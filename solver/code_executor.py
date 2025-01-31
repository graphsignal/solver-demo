import logging
import asyncio
import os
import sys
import tempfile

# configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

async def execute_code(code: str, input_data: str = "", timeout=5) -> tuple[str, str]:
    try:
        logger.debug("Executing code:")
        logger.debug(input_data)

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
                timeout=timeout
            )

            logger.debug(f"Execution stdout: {stdout.decode()}")

            return stdout.decode(), stderr.decode()
        except asyncio.TimeoutError:
            process.kill()
            await process.wait()
            return "", f"Execution timed out. Timeout {timeout} seconds."
    except Exception as e:
        raise e
    finally:
        try:
            os.remove(tmp_file_path)
        except:
            pass
