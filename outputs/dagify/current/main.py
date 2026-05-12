import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.add_grand_finale import add_grand_finale
from code.generate_character_profiles import generate_character_profiles
from code.generate_story_outline import generate_story_outline
from code.generate_story_setting import generate_story_setting
from code.write_chapter_1 import write_chapter_1
from code.write_chapter_2 import write_chapter_2
from code.write_chapter_3 import write_chapter_3

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

add_grand_finale_async = make_async(add_grand_finale)
generate_character_profiles_async = make_async(generate_character_profiles)
generate_story_outline_async = make_async(generate_story_outline)
generate_story_setting_async = make_async(generate_story_setting)
write_chapter_1_async = make_async(write_chapter_1)
write_chapter_2_async = make_async(write_chapter_2)
write_chapter_3_async = make_async(write_chapter_3)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: generate_story_setting, generate_character_profiles, generate_story_outline
    async def run_generate_story_setting():
        # Call the async version of generate_story_setting with results from dependencies
        return await generate_story_setting_async(user_input)

    async def run_generate_character_profiles():
        # Call the async version of generate_character_profiles with results from dependencies
        return await generate_character_profiles_async(user_input)

    async def run_generate_story_outline():
        # Call the async version of generate_story_outline with results from dependencies
        return await generate_story_outline_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_generate_story_setting(), run_generate_character_profiles(), run_generate_story_outline())
    results['generate_story_setting'] = level_0_results[0]
    results['generate_character_profiles'] = level_0_results[1]
    results['generate_story_outline'] = level_0_results[2]

    # Level 1: write_chapter_1
    async def run_write_chapter_1():
        # Call the async version of write_chapter_1 with results from dependencies
        return await write_chapter_1_async(results['generate_story_outline'], results['generate_character_profiles'], results['generate_story_setting'])

    # Run level 1 nodes in parallel
    results['write_chapter_1'] = await run_write_chapter_1()

    # Level 2: write_chapter_2
    async def run_write_chapter_2():
        # Call the async version of write_chapter_2 with results from dependencies
        return await write_chapter_2_async(results['write_chapter_1'], results['generate_story_outline'], results['generate_character_profiles'], results['generate_story_setting'])

    # Run level 2 nodes in parallel
    results['write_chapter_2'] = await run_write_chapter_2()

    # Level 3: write_chapter_3
    async def run_write_chapter_3():
        # Call the async version of write_chapter_3 with results from dependencies
        return await write_chapter_3_async(results['write_chapter_2'], results['generate_story_outline'], results['generate_character_profiles'], results['generate_story_setting'])

    # Run level 3 nodes in parallel
    results['write_chapter_3'] = await run_write_chapter_3()

    # Level 4: add_grand_finale
    async def run_add_grand_finale():
        # Call the async version of add_grand_finale with results from dependencies
        return await add_grand_finale_async(results['write_chapter_3'])

    # Run level 4 nodes in parallel
    results['add_grand_finale'] = await run_add_grand_finale()

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
