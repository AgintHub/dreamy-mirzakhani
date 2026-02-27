import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.authenticate_pico_credentials import authenticate_pico_credentials
from code.establish_pico_connection import establish_pico_connection
from code.identify_dropcopy_source import identify_dropcopy_source
from code.merge_stored_dropcopy import merge_stored_dropcopy
from code.notify_dropcopy_pull import notify_dropcopy_pull
from code.process_dropcopy_part1 import process_dropcopy_part1
from code.process_dropcopy_part2 import process_dropcopy_part2
from code.process_dropcopy_part3 import process_dropcopy_part3
from code.pull_dropcopy import pull_dropcopy
from code.store_dropcopy_part1 import store_dropcopy_part1
from code.store_dropcopy_part2 import store_dropcopy_part2
from code.store_dropcopy_part3 import store_dropcopy_part3
from code.verify_dropcopy_integrity import verify_dropcopy_integrity

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

authenticate_pico_credentials_async = make_async(authenticate_pico_credentials)
establish_pico_connection_async = make_async(establish_pico_connection)
identify_dropcopy_source_async = make_async(identify_dropcopy_source)
merge_stored_dropcopy_async = make_async(merge_stored_dropcopy)
notify_dropcopy_pull_async = make_async(notify_dropcopy_pull)
process_dropcopy_part1_async = make_async(process_dropcopy_part1)
process_dropcopy_part2_async = make_async(process_dropcopy_part2)
process_dropcopy_part3_async = make_async(process_dropcopy_part3)
pull_dropcopy_async = make_async(pull_dropcopy)
store_dropcopy_part1_async = make_async(store_dropcopy_part1)
store_dropcopy_part2_async = make_async(store_dropcopy_part2)
store_dropcopy_part3_async = make_async(store_dropcopy_part3)
verify_dropcopy_integrity_async = make_async(verify_dropcopy_integrity)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: establish_pico_connection
    async def run_establish_pico_connection():
        # Call the async version of establish_pico_connection with results from dependencies
        return await establish_pico_connection_async(user_input)

    # Run level 0 nodes in parallel
    results['establish_pico_connection'] = await run_establish_pico_connection()

    # Level 1: authenticate_pico_credentials
    async def run_authenticate_pico_credentials():
        # Call the async version of authenticate_pico_credentials with results from dependencies
        return await authenticate_pico_credentials_async(results['establish_pico_connection'])

    # Run level 1 nodes in parallel
    results['authenticate_pico_credentials'] = await run_authenticate_pico_credentials()

    # Level 2: identify_dropcopy_source
    async def run_identify_dropcopy_source():
        # Call the async version of identify_dropcopy_source with results from dependencies
        return await identify_dropcopy_source_async(results['authenticate_pico_credentials'])

    # Run level 2 nodes in parallel
    results['identify_dropcopy_source'] = await run_identify_dropcopy_source()

    # Level 3: pull_dropcopy
    async def run_pull_dropcopy():
        # Call the async version of pull_dropcopy with results from dependencies
        return await pull_dropcopy_async(results['identify_dropcopy_source'])

    # Run level 3 nodes in parallel
    results['pull_dropcopy'] = await run_pull_dropcopy()

    # Level 4: process_dropcopy_part1, process_dropcopy_part2, process_dropcopy_part3
    async def run_process_dropcopy_part1():
        # Call the async version of process_dropcopy_part1 with results from dependencies
        return await process_dropcopy_part1_async(results['pull_dropcopy'])

    async def run_process_dropcopy_part2():
        # Call the async version of process_dropcopy_part2 with results from dependencies
        return await process_dropcopy_part2_async(results['pull_dropcopy'])

    async def run_process_dropcopy_part3():
        # Call the async version of process_dropcopy_part3 with results from dependencies
        return await process_dropcopy_part3_async(results['pull_dropcopy'])

    # Run level 4 nodes in parallel
    level_4_results = await asyncio.gather(run_process_dropcopy_part1(), run_process_dropcopy_part2(), run_process_dropcopy_part3())
    results['process_dropcopy_part1'] = level_4_results[0]
    results['process_dropcopy_part2'] = level_4_results[1]
    results['process_dropcopy_part3'] = level_4_results[2]

    # Level 5: store_dropcopy_part3, store_dropcopy_part2, store_dropcopy_part1
    async def run_store_dropcopy_part3():
        # Call the async version of store_dropcopy_part3 with results from dependencies
        return await store_dropcopy_part3_async(results['process_dropcopy_part3'])

    async def run_store_dropcopy_part2():
        # Call the async version of store_dropcopy_part2 with results from dependencies
        return await store_dropcopy_part2_async(results['process_dropcopy_part2'])

    async def run_store_dropcopy_part1():
        # Call the async version of store_dropcopy_part1 with results from dependencies
        return await store_dropcopy_part1_async(results['process_dropcopy_part1'])

    # Run level 5 nodes in parallel
    level_5_results = await asyncio.gather(run_store_dropcopy_part3(), run_store_dropcopy_part2(), run_store_dropcopy_part1())
    results['store_dropcopy_part3'] = level_5_results[0]
    results['store_dropcopy_part2'] = level_5_results[1]
    results['store_dropcopy_part1'] = level_5_results[2]

    # Level 6: merge_stored_dropcopy
    async def run_merge_stored_dropcopy():
        # Call the async version of merge_stored_dropcopy with results from dependencies
        return await merge_stored_dropcopy_async(results['store_dropcopy_part1'], results['store_dropcopy_part2'], results['store_dropcopy_part3'])

    # Run level 6 nodes in parallel
    results['merge_stored_dropcopy'] = await run_merge_stored_dropcopy()

    # Level 7: verify_dropcopy_integrity
    async def run_verify_dropcopy_integrity():
        # Call the async version of verify_dropcopy_integrity with results from dependencies
        return await verify_dropcopy_integrity_async(results['merge_stored_dropcopy'])

    # Run level 7 nodes in parallel
    results['verify_dropcopy_integrity'] = await run_verify_dropcopy_integrity()

    # Level 8: notify_dropcopy_pull
    async def run_notify_dropcopy_pull():
        # Call the async version of notify_dropcopy_pull with results from dependencies
        return await notify_dropcopy_pull_async(results['verify_dropcopy_integrity'])

    # Run level 8 nodes in parallel
    results['notify_dropcopy_pull'] = await run_notify_dropcopy_pull()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
