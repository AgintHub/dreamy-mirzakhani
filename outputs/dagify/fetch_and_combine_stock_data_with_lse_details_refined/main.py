import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.construct_lse_api_request import construct_lse_api_request
from code.construct_nasdaq_api_request import construct_nasdaq_api_request
from code.construct_nyse_api_request import construct_nyse_api_request
from code.construct_toronto_stock_exchange_api_request import construct_toronto_stock_exchange_api_request
from code.fetch_lse_stock_data import fetch_lse_stock_data
from code.fetch_nasdaq_stock_data import fetch_nasdaq_stock_data
from code.fetch_nyse_stock_data import fetch_nyse_stock_data
from code.fetch_toronto_stock_exchange_stock_data import fetch_toronto_stock_exchange_stock_data
from code.identify_lse_stocks import identify_lse_stocks
from code.identify_nasdaq_stocks import identify_nasdaq_stocks
from code.identify_nyse_stocks import identify_nyse_stocks
from code.identify_toronto_stock_exchange_stocks import identify_toronto_stock_exchange_stocks
from code.normalize_combined_stock_data import normalize_combined_stock_data
from code.parse_lse_stock_data import parse_lse_stock_data
from code.parse_nasdaq_stock_data import parse_nasdaq_stock_data
from code.parse_nyse_stock_data import parse_nyse_stock_data
from code.parse_toronto_stock_exchange_stock_data import parse_toronto_stock_exchange_stock_data
from code.repartition_combined_stock_data import repartition_combined_stock_data
from code.store_combined_stock_data import store_combined_stock_data

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

construct_lse_api_request_async = make_async(construct_lse_api_request)
construct_nasdaq_api_request_async = make_async(construct_nasdaq_api_request)
construct_nyse_api_request_async = make_async(construct_nyse_api_request)
construct_toronto_stock_exchange_api_request_async = make_async(construct_toronto_stock_exchange_api_request)
fetch_lse_stock_data_async = make_async(fetch_lse_stock_data)
fetch_nasdaq_stock_data_async = make_async(fetch_nasdaq_stock_data)
fetch_nyse_stock_data_async = make_async(fetch_nyse_stock_data)
fetch_toronto_stock_exchange_stock_data_async = make_async(fetch_toronto_stock_exchange_stock_data)
identify_lse_stocks_async = make_async(identify_lse_stocks)
identify_nasdaq_stocks_async = make_async(identify_nasdaq_stocks)
identify_nyse_stocks_async = make_async(identify_nyse_stocks)
identify_toronto_stock_exchange_stocks_async = make_async(identify_toronto_stock_exchange_stocks)
normalize_combined_stock_data_async = make_async(normalize_combined_stock_data)
parse_lse_stock_data_async = make_async(parse_lse_stock_data)
parse_nasdaq_stock_data_async = make_async(parse_nasdaq_stock_data)
parse_nyse_stock_data_async = make_async(parse_nyse_stock_data)
parse_toronto_stock_exchange_stock_data_async = make_async(parse_toronto_stock_exchange_stock_data)
repartition_combined_stock_data_async = make_async(repartition_combined_stock_data)
store_combined_stock_data_async = make_async(store_combined_stock_data)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: identify_nyse_stocks, identify_toronto_stock_exchange_stocks, identify_nasdaq_stocks, identify_lse_stocks
    async def run_identify_nyse_stocks():
        # Call the async version of identify_nyse_stocks with results from dependencies
        return await identify_nyse_stocks_async(user_input)

    async def run_identify_toronto_stock_exchange_stocks():
        # Call the async version of identify_toronto_stock_exchange_stocks with results from dependencies
        return await identify_toronto_stock_exchange_stocks_async(user_input)

    async def run_identify_nasdaq_stocks():
        # Call the async version of identify_nasdaq_stocks with results from dependencies
        return await identify_nasdaq_stocks_async(user_input)

    async def run_identify_lse_stocks():
        # Call the async version of identify_lse_stocks with results from dependencies
        return await identify_lse_stocks_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_identify_nyse_stocks(), run_identify_toronto_stock_exchange_stocks(), run_identify_nasdaq_stocks(), run_identify_lse_stocks())
    results['identify_nyse_stocks'] = level_0_results[0]
    results['identify_toronto_stock_exchange_stocks'] = level_0_results[1]
    results['identify_nasdaq_stocks'] = level_0_results[2]
    results['identify_lse_stocks'] = level_0_results[3]

    # Level 1: construct_toronto_stock_exchange_api_request, construct_nasdaq_api_request, construct_nyse_api_request, construct_lse_api_request
    async def run_construct_toronto_stock_exchange_api_request():
        # Call the async version of construct_toronto_stock_exchange_api_request with results from dependencies
        return await construct_toronto_stock_exchange_api_request_async(results['identify_toronto_stock_exchange_stocks'])

    async def run_construct_nasdaq_api_request():
        # Call the async version of construct_nasdaq_api_request with results from dependencies
        return await construct_nasdaq_api_request_async(results['identify_nasdaq_stocks'])

    async def run_construct_nyse_api_request():
        # Call the async version of construct_nyse_api_request with results from dependencies
        return await construct_nyse_api_request_async(results['identify_nyse_stocks'])

    async def run_construct_lse_api_request():
        # Call the async version of construct_lse_api_request with results from dependencies
        return await construct_lse_api_request_async(results['identify_lse_stocks'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_construct_toronto_stock_exchange_api_request(), run_construct_nasdaq_api_request(), run_construct_nyse_api_request(), run_construct_lse_api_request())
    results['construct_toronto_stock_exchange_api_request'] = level_1_results[0]
    results['construct_nasdaq_api_request'] = level_1_results[1]
    results['construct_nyse_api_request'] = level_1_results[2]
    results['construct_lse_api_request'] = level_1_results[3]

    # Level 2: fetch_lse_stock_data, fetch_nasdaq_stock_data, fetch_toronto_stock_exchange_stock_data, fetch_nyse_stock_data
    async def run_fetch_lse_stock_data():
        # Call the async version of fetch_lse_stock_data with results from dependencies
        return await fetch_lse_stock_data_async(results['construct_lse_api_request'])

    async def run_fetch_nasdaq_stock_data():
        # Call the async version of fetch_nasdaq_stock_data with results from dependencies
        return await fetch_nasdaq_stock_data_async(results['construct_nasdaq_api_request'])

    async def run_fetch_toronto_stock_exchange_stock_data():
        # Call the async version of fetch_toronto_stock_exchange_stock_data with results from dependencies
        return await fetch_toronto_stock_exchange_stock_data_async(results['construct_toronto_stock_exchange_api_request'])

    async def run_fetch_nyse_stock_data():
        # Call the async version of fetch_nyse_stock_data with results from dependencies
        return await fetch_nyse_stock_data_async(results['construct_nyse_api_request'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_fetch_lse_stock_data(), run_fetch_nasdaq_stock_data(), run_fetch_toronto_stock_exchange_stock_data(), run_fetch_nyse_stock_data())
    results['fetch_lse_stock_data'] = level_2_results[0]
    results['fetch_nasdaq_stock_data'] = level_2_results[1]
    results['fetch_toronto_stock_exchange_stock_data'] = level_2_results[2]
    results['fetch_nyse_stock_data'] = level_2_results[3]

    # Level 3: parse_toronto_stock_exchange_stock_data, parse_nasdaq_stock_data, parse_lse_stock_data, parse_nyse_stock_data
    async def run_parse_toronto_stock_exchange_stock_data():
        # Call the async version of parse_toronto_stock_exchange_stock_data with results from dependencies
        return await parse_toronto_stock_exchange_stock_data_async(results['fetch_toronto_stock_exchange_stock_data'])

    async def run_parse_nasdaq_stock_data():
        # Call the async version of parse_nasdaq_stock_data with results from dependencies
        return await parse_nasdaq_stock_data_async(results['fetch_nasdaq_stock_data'])

    async def run_parse_lse_stock_data():
        # Call the async version of parse_lse_stock_data with results from dependencies
        return await parse_lse_stock_data_async(results['fetch_lse_stock_data'])

    async def run_parse_nyse_stock_data():
        # Call the async version of parse_nyse_stock_data with results from dependencies
        return await parse_nyse_stock_data_async(results['fetch_nyse_stock_data'])

    # Run level 3 nodes in parallel
    level_3_results = await asyncio.gather(run_parse_toronto_stock_exchange_stock_data(), run_parse_nasdaq_stock_data(), run_parse_lse_stock_data(), run_parse_nyse_stock_data())
    results['parse_toronto_stock_exchange_stock_data'] = level_3_results[0]
    results['parse_nasdaq_stock_data'] = level_3_results[1]
    results['parse_lse_stock_data'] = level_3_results[2]
    results['parse_nyse_stock_data'] = level_3_results[3]

    # Level 4: store_combined_stock_data
    async def run_store_combined_stock_data():
        # Call the async version of store_combined_stock_data with results from dependencies
        return await store_combined_stock_data_async(results['parse_lse_stock_data'], results['parse_nasdaq_stock_data'], results['parse_nyse_stock_data'], results['parse_toronto_stock_exchange_stock_data'])

    # Run level 4 nodes in parallel
    results['store_combined_stock_data'] = await run_store_combined_stock_data()

    # Level 5: normalize_combined_stock_data
    async def run_normalize_combined_stock_data():
        # Call the async version of normalize_combined_stock_data with results from dependencies
        return await normalize_combined_stock_data_async(results['store_combined_stock_data'])

    # Run level 5 nodes in parallel
    results['normalize_combined_stock_data'] = await run_normalize_combined_stock_data()

    # Level 6: repartition_combined_stock_data
    async def run_repartition_combined_stock_data():
        # Call the async version of repartition_combined_stock_data with results from dependencies
        return await repartition_combined_stock_data_async(results['normalize_combined_stock_data'])

    # Run level 6 nodes in parallel
    results['repartition_combined_stock_data'] = await run_repartition_combined_stock_data()

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
