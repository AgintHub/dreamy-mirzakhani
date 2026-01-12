import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.build_sample_database import build_sample_database
from code.create_app_interface import create_app_interface
from code.extract_audio_features import extract_audio_features
from code.generate_song_links import generate_song_links
from code.integrate_app_components import integrate_app_components
from code.load_audio_snippet import load_audio_snippet
from code.query_sample_database import query_sample_database
from code.rank_and_filter_matches import rank_and_filter_matches
from code.retrieve_song_metadata import retrieve_song_metadata
from code.test_and_refine_app import test_and_refine_app

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

build_sample_database_async = make_async(build_sample_database)
create_app_interface_async = make_async(create_app_interface)
extract_audio_features_async = make_async(extract_audio_features)
generate_song_links_async = make_async(generate_song_links)
integrate_app_components_async = make_async(integrate_app_components)
load_audio_snippet_async = make_async(load_audio_snippet)
query_sample_database_async = make_async(query_sample_database)
rank_and_filter_matches_async = make_async(rank_and_filter_matches)
retrieve_song_metadata_async = make_async(retrieve_song_metadata)
test_and_refine_app_async = make_async(test_and_refine_app)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: create_app_interface, load_audio_snippet, build_sample_database
    async def run_create_app_interface():
        # Call the async version of create_app_interface with results from dependencies
        return await create_app_interface_async(user_input)

    async def run_load_audio_snippet():
        # Call the async version of load_audio_snippet with results from dependencies
        return await load_audio_snippet_async(user_input)

    async def run_build_sample_database():
        # Call the async version of build_sample_database with results from dependencies
        return await build_sample_database_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_create_app_interface(), run_load_audio_snippet(), run_build_sample_database())
    results['create_app_interface'] = level_0_results[0]
    results['load_audio_snippet'] = level_0_results[1]
    results['build_sample_database'] = level_0_results[2]

    # Level 1: extract_audio_features
    async def run_extract_audio_features():
        # Call the async version of extract_audio_features with results from dependencies
        return await extract_audio_features_async(results['load_audio_snippet'])

    # Run level 1 nodes in parallel
    results['extract_audio_features'] = await run_extract_audio_features()

    # Level 2: query_sample_database
    async def run_query_sample_database():
        # Call the async version of query_sample_database with results from dependencies
        return await query_sample_database_async(results['extract_audio_features'], results['build_sample_database'])

    # Run level 2 nodes in parallel
    results['query_sample_database'] = await run_query_sample_database()

    # Level 3: rank_and_filter_matches
    async def run_rank_and_filter_matches():
        # Call the async version of rank_and_filter_matches with results from dependencies
        return await rank_and_filter_matches_async(results['query_sample_database'])

    # Run level 3 nodes in parallel
    results['rank_and_filter_matches'] = await run_rank_and_filter_matches()

    # Level 4: retrieve_song_metadata
    async def run_retrieve_song_metadata():
        # Call the async version of retrieve_song_metadata with results from dependencies
        return await retrieve_song_metadata_async(results['rank_and_filter_matches'])

    # Run level 4 nodes in parallel
    results['retrieve_song_metadata'] = await run_retrieve_song_metadata()

    # Level 5: generate_song_links
    async def run_generate_song_links():
        # Call the async version of generate_song_links with results from dependencies
        return await generate_song_links_async(results['retrieve_song_metadata'])

    # Run level 5 nodes in parallel
    results['generate_song_links'] = await run_generate_song_links()

    # Level 6: integrate_app_components
    async def run_integrate_app_components():
        # Call the async version of integrate_app_components with results from dependencies
        return await integrate_app_components_async(results['load_audio_snippet'], results['generate_song_links'], results['create_app_interface'])

    # Run level 6 nodes in parallel
    results['integrate_app_components'] = await run_integrate_app_components()

    # Level 7: test_and_refine_app
    async def run_test_and_refine_app():
        # Call the async version of test_and_refine_app with results from dependencies
        return await test_and_refine_app_async(results['integrate_app_components'])

    # Run level 7 nodes in parallel
    results['test_and_refine_app'] = await run_test_and_refine_app()

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
