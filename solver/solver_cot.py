import logging
import asyncio
import csv
import os
from pathlib import Path
import sys
import tempfile
from typing import List, Dict
import json
from openai_chat import OpenAIChat
from code_executor import execute_code

# configure logger
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# import and initialize Graphsignal
# add GRAPSIGNAL_API_KEY to your environment variables
import graphsignal
graphsignal.configure(deployment='solver-cot', debug_mode=True)


# Constants
CSV_FILE_PATH = Path('./problems/codeforces.csv') 
SOLUTIONS_DIR = Path('./solutions')
MAX_RETRIES = 3
TIMEOUT_SECONDS = 5

async def read_csv(file_path: Path) -> List[Dict[str, str]]:
    loop = asyncio.get_event_loop()
    problems = []
    def read():
        with file_path.open('r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    problems = await loop.run_in_executor(None, read)
    return problems

async def process_problem(problem: Dict[str, str]):
    contest = problem.get('contest', 'unknown_contest')
    problem_name = problem.get('problem_name', 'unknown_problem')
    problem_statement = problem.get('problem_statement', '')
    problem_tags = problem.get('problem_tags', '')
    problem_id = f"{contest}-{problem_name}"

    graphsignal.set_context_tag('task_id', problem_id, append_uuid=True)

    logger.debug(f"Processing problem: {problem_id}")

    solutions_dir = SOLUTIONS_DIR
    solutions_dir.mkdir(parents=True, exist_ok=True)
    solution_file = solutions_dir / f"{problem_id}.py"

    chat = OpenAIChat("You are a helpful assistant who solves coding problems.")
    chat.user(f"Problem id: {problem_id}\nStatement: {problem_statement}\nTags: {problem_tags}")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.debug(f"Attempt {attempt} for problem: {problem_id}")

            if attempt == 1:
                chat.user("Please provide a step-by-step plan to solve the problem.")
            else:
                chat.user("Please provide a revised step-by-step plan taking into account previous errors.")
            plan = await chat.generate_completion()
            chat.assistant(plan)

            chat.user("Provide a runnable Python code that includes solution function based on the above plan and a verification call to solution function that checks the return value, and prints 'verified' if correct. If incorrect, prints possible reason with actual and expected result. The program should not ask for any external input.")
            solution_code = await chat.generate_code()
            chat.assistant(solution_code)

            with graphsignal.trace('execute_code'):
                solution_stdout, solution_stderr = await execute_code(solution_code, timeout=TIMEOUT_SECONDS)
            logger.debug(f"Verification result for {problem_id}: {solution_stdout}")
            if 'verified' in solution_stdout.lower():
                with solution_file.open('w', encoding='utf-8') as f:
                    f.write(f"'''\nProblem id: {problem_id}\nStatement: {problem_statement}\nTags: {problem_tags}\n'''\n\n{solution_code}")
                logger.debug(f"Solution for {problem_id} verified and saved.")
                break
            elif solution_stderr:
                chat.user(f"Verification error: {solution_stderr}")
                logger.debug(f"Verification error for {problem_id}: {solution_stderr}")
            else:
                chat.user(f"Verification error: {solution_stdout}")
                logger.debug(f"Verification error for {problem_id}: Unexpected output.")
        except Exception as e:
            logger.debug(f"Error processing problem {problem_id}: {e}")
        finally:
            if attempt == MAX_RETRIES:
                logger.debug(f"Max retries reached for problem: {problem_id}. Moving to next problem.")

    graphsignal.remove_context_tag('task_id')

    await chat.close()

async def main():
    # Check if CSV file exists
    if not CSV_FILE_PATH.exists():
        logger.debug(f"CSV file not found at {CSV_FILE_PATH}")
        return

    # Read problems from CSV
    problems = await read_csv(CSV_FILE_PATH)
    logger.debug(f"Total problems to process: {len(problems)}")

    # Process each problem sequentially or concurrently
    #tasks = [process_problem(problem) for problem in problems]
    #await asyncio.gather(*tasks)

    for problem in problems:
        await process_problem(problem)

if __name__ == "__main__":
    asyncio.run(main())