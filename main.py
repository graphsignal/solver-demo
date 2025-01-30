import asyncio
import csv
import os
from pathlib import Path
import sys
import tempfile
from typing import List, Dict
import json

import openai
from openai import AsyncOpenAI
from openai import OpenAIError

# Constants
CSV_FILE_PATH = Path('./problems/codeforces.csv') 
SOLUTIONS_DIR = Path('./solutions')
MAX_RETRIES = 3
TIMEOUT_SECONDS = 5
MODEL_NAME = "gpt-4o"

# Initialize OpenAI client
#openai.api_key = os.getenv('OPENAI_API_KEY')
client = AsyncOpenAI()

async def read_csv(file_path: Path) -> List[Dict[str, str]]:
    loop = asyncio.get_event_loop()
    problems = []
    def read():
        with file_path.open('r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    problems = await loop.run_in_executor(None, read)
    return problems

async def generate_completion(messages: List[Dict[str, str]]) -> str:
    try:
        print(f"-----Messages: {messages}")
        print("-----Generating completion...")

        completion = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )

        completion_content = completion.choices[0].message.content.strip()
        print(f"-----Completion: {completion_content}")
        return completion_content
    except OpenAIError as e:
        raise e


async def generate_code(messages: List[Dict[str, str]]) -> str:
    try:
        messages.append({"role": "user", "content": "Pass generated Python code to 'code' argument of 'execute_code' function."})
        print(f"-----Messages: {messages}")
        print("-----Generating code...")

        tools = [
            {
                "type": "function",
                "function": {
                    "name": "execute_code",
                    "description": "Executes Python code",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "Python code to execute"
                            }
                        },
                        "required": ["code"]
                    }
                }
            }
        ]

        completion = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        print(f"-----Completion: {completion}")
        args_json = completion.choices[0].message.tool_calls[0].function.arguments
        args = json.loads(args_json)
        code = args['code'].strip()

        print(f"-----Code: {code}")
        return code
    except OpenAIError as e:
        raise e


async def execute_code(code: str, input_data: str = "") -> tuple[str, str]:
    try:
        print("-----Executing code:")
        print(input_data)

        with tempfile.NamedTemporaryFile('w+', suffix='.py', delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file_path = tmp_file.name

        process = await asyncio.create_subprocess_exec(
            sys.executable, tmp_file_path,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(input=input_data.encode()),
                timeout=TIMEOUT_SECONDS
            )

            print(f"-----Execution stdout: {stdout.decode()}")

            return stdout.decode(), stderr.decode()
        except asyncio.TimeoutError:
            process.kill()
            await process.wait()
            return "", "Execution timed out."
    except Exception as e:
        raise e
    finally:
        try:
            os.remove(tmp_file_path)
        except:
            pass

async def process_problem(problem: Dict[str, str]):
    contest = problem.get('contest', 'unknown_contest')
    problem_name = problem.get('problem_name', 'unknown_problem')
    problem_statement = problem.get('problem_statement', '')
    problem_tags = problem.get('problem_tags', '')

    print(f"-----Processing Problem: {problem_name} from Contest: {contest}")
    print(f"-----Problem Statement: {problem_statement}")

    solutions_dir = SOLUTIONS_DIR
    solutions_dir.mkdir(parents=True, exist_ok=True)
    solution_file = solutions_dir / f"{problem_name}.py"

    context = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Problem Name: {problem_name}\nStatement: {problem_statement}\nTags: {problem_tags}"}
    ]

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Attempt {attempt} for problem: {problem_name}")

            if attempt == 1:
                context.append({"role": "user", "content": "Generate a step-by-step plan to solve the above problem."})
            else:
                context.append({"role": "user", "content": "Please provide a revised step-by-step plan taking into account previous errors."})
            plan = await generate_completion(context)
            context.append({"role": "assistant", "content": plan})

            context.append({"role": "user", "content": "Provide a runnable Python code that includes solution function based on the above plan and a verification call to solution function that checks the return value, and prints 'correct' or 'incorrect' respectively. The program should not ask for any external input."})
            solution_code = await generate_code(context)
            context.append({"role": "assistant", "content": f'Generated solution code: \n{solution_code}'})

            solution_stdout, solution_stderr = await execute_code(solution_code)
            solution_result = solution_stdout.strip().lower()
            print(f"-----Verification result for {problem_name}: {solution_result}")
            if solution_result == "correct":
                with solution_file.open('w', encoding='utf-8') as f:
                    f.write(solution_code)
                print(f"-----Solution for {problem_name} verified and saved.")
                break
            elif solution_result == "incorrect":
                context.append({"role": "user", "content": "The solution was incorrect."})
                print(f"-----Solution for {problem_name} was incorrect. Retrying...")
            elif solution_stderr:
                context.append({"role": "user", "content": f"Verification error: {solution_stderr}"})
                print(f"-----Verification error for {problem_name}: {solution_stderr}")
            else:
                context.append({"role": "user", "content": "Verification error: No output."})
                print(f"-----Verification error for {problem_name}: No output.")
        except Exception as e:
            print(f"-----Error processing problem {problem_name}: {e}")
        finally:
            if attempt == MAX_RETRIES:
                print(f"-----Max retries reached for problem: {problem_name}. Moving to next problem.")

async def main():
    # Check if CSV file exists
    if not CSV_FILE_PATH.exists():
        print(f"CSV file not found at {CSV_FILE_PATH}")
        return

    # Read problems from CSV
    problems = await read_csv(CSV_FILE_PATH)
    print(f"Total problems to process: {len(problems)}")

    # Process each problem sequentially or concurrently
    #tasks = [process_problem(problem) for problem in problems]
    #await asyncio.gather(*tasks)

    for problem in problems:
        await process_problem(problem)

if __name__ == "__main__":
    asyncio.run(main())