import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.build_app_interface import build_app_interface
from code.create_playlist import create_playlist
from code.extract_song_metadata import extract_song_metadata
from code.identify_sampled_songs import identify_sampled_songs
from code.integrate_features import integrate_features
from code.list_musicians import list_musicians
from code.offer_playlist_to_user import offer_playlist_to_user
from code.preprocess_audio_data import preprocess_audio_data
from code.record_audio_snippet import record_audio_snippet
from code.redirect_to_musicians_pages import redirect_to_musicians_pages
from code.test_app_functionality import test_app_functionality

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

build_app_interface_async = make_async(build_app_interface)
create_playlist_async = make_async(create_playlist)
extract_song_metadata_async = make_async(extract_song_metadata)
identify_sampled_songs_async = make_async(identify_sampled_songs)
integrate_features_async = make_async(integrate_features)
list_musicians_async = make_async(list_musicians)
offer_playlist_to_user_async = make_async(offer_playlist_to_user)
preprocess_audio_data_async = make_async(preprocess_audio_data)
record_audio_snippet_async = make_async(record_audio_snippet)
redirect_to_musicians_pages_async = make_async(redirect_to_musicians_pages)
test_app_functionality_async = make_async(test_app_functionality)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: build_app_interface, record_audio_snippet
    async def run_build_app_interface():
        # Call the async version of build_app_interface with results from dependencies
        return await build_app_interface_async(user_input)

    async def run_record_audio_snippet():
        # Call the async version of record_audio_snippet with results from dependencies
        return await record_audio_snippet_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_build_app_interface(), run_record_audio_snippet())
    results['build_app_interface'] = level_0_results[0]
    results['record_audio_snippet'] = level_0_results[1]

    # Level 1: preprocess_audio_data
    async def run_preprocess_audio_data():
        # Call the async version of preprocess_audio_data with results from dependencies
        return await preprocess_audio_data_async(results['record_audio_snippet'])

    # Run level 1 nodes in parallel
    results['preprocess_audio_data'] = await run_preprocess_audio_data()

    # Level 2: identify_sampled_songs
    async def run_identify_sampled_songs():
        # Call the async version of identify_sampled_songs with results from dependencies
        return await identify_sampled_songs_async(results['preprocess_audio_data'])

    # Run level 2 nodes in parallel
    results['identify_sampled_songs'] = await run_identify_sampled_songs()

    # Level 3: extract_song_metadata
    async def run_extract_song_metadata():
        # Call the async version of extract_song_metadata with results from dependencies
        return await extract_song_metadata_async(results['identify_sampled_songs'])

    # Run level 3 nodes in parallel
    results['extract_song_metadata'] = await run_extract_song_metadata()

    # Level 4: list_musicians
    async def run_list_musicians():
        # Call the async version of list_musicians with results from dependencies
        return await list_musicians_async(results['extract_song_metadata'])

    # Run level 4 nodes in parallel
    results['list_musicians'] = await run_list_musicians()

    # Level 5: redirect_to_musicians_pages, create_playlist
    async def run_redirect_to_musicians_pages():
        # Call the async version of redirect_to_musicians_pages with results from dependencies
        return await redirect_to_musicians_pages_async(results['list_musicians'])

    async def run_create_playlist():
        # Call the async version of create_playlist with results from dependencies
        return await create_playlist_async(results['list_musicians'])

    # Run level 5 nodes in parallel
    level_5_results = await asyncio.gather(run_redirect_to_musicians_pages(), run_create_playlist())
    results['redirect_to_musicians_pages'] = level_5_results[0]
    results['create_playlist'] = level_5_results[1]

    # Level 6: offer_playlist_to_user
    async def run_offer_playlist_to_user():
        # Call the async version of offer_playlist_to_user with results from dependencies
        return await offer_playlist_to_user_async(results['create_playlist'])

    # Run level 6 nodes in parallel
    results['offer_playlist_to_user'] = await run_offer_playlist_to_user()

    # Level 7: integrate_features
    async def run_integrate_features():
        # Call the async version of integrate_features with results from dependencies
        return await integrate_features_async(results['build_app_interface'], results['redirect_to_musicians_pages'], results['offer_playlist_to_user'])

    # Run level 7 nodes in parallel
    results['integrate_features'] = await run_integrate_features()

    # Level 8: test_app_functionality
    async def run_test_app_functionality():
        # Call the async version of test_app_functionality with results from dependencies
        return await test_app_functionality_async(results['integrate_features'])

    # Run level 8 nodes in parallel
    results['test_app_functionality'] = await run_test_app_functionality()

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
