import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_backtest_results import analyze_backtest_results
from code.build_risk_rules import build_risk_rules
from code.calculate_position_sizing import calculate_position_sizing
from code.choose_strategy_approach import choose_strategy_approach
from code.compile_strategy_documentation import compile_strategy_documentation
from code.define_strategy_objective import define_strategy_objective
from code.deploy_automated_backtest import deploy_automated_backtest
from code.develop_entry_rules import develop_entry_rules
from code.develop_exit_rules import develop_exit_rules
from code.execute_in_sample_backtest import execute_in_sample_backtest
from code.generate_strategy_presentation import generate_strategy_presentation
from code.implement_slippage_model import implement_slippage_model
from code.optimize_parameters import optimize_parameters
from code.preprocess_data import preprocess_data
from code.select_data_sources import select_data_sources
from code.set_backtest_parameters import set_backtest_parameters
from code.set_performance_benchmarks import set_performance_benchmarks
from code.validate_out_of_sample import validate_out_of_sample

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

analyze_backtest_results_async = make_async(analyze_backtest_results)
build_risk_rules_async = make_async(build_risk_rules)
calculate_position_sizing_async = make_async(calculate_position_sizing)
choose_strategy_approach_async = make_async(choose_strategy_approach)
compile_strategy_documentation_async = make_async(compile_strategy_documentation)
define_strategy_objective_async = make_async(define_strategy_objective)
deploy_automated_backtest_async = make_async(deploy_automated_backtest)
develop_entry_rules_async = make_async(develop_entry_rules)
develop_exit_rules_async = make_async(develop_exit_rules)
execute_in_sample_backtest_async = make_async(execute_in_sample_backtest)
generate_strategy_presentation_async = make_async(generate_strategy_presentation)
implement_slippage_model_async = make_async(implement_slippage_model)
optimize_parameters_async = make_async(optimize_parameters)
preprocess_data_async = make_async(preprocess_data)
select_data_sources_async = make_async(select_data_sources)
set_backtest_parameters_async = make_async(set_backtest_parameters)
set_performance_benchmarks_async = make_async(set_performance_benchmarks)
validate_out_of_sample_async = make_async(validate_out_of_sample)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: define_strategy_objective, select_data_sources
    async def run_define_strategy_objective():
        # Call the async version of define_strategy_objective with results from dependencies
        return await define_strategy_objective_async(user_input)

    async def run_select_data_sources():
        # Call the async version of select_data_sources with results from dependencies
        return await select_data_sources_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_define_strategy_objective(), run_select_data_sources())
    results['define_strategy_objective'] = level_0_results[0]
    results['select_data_sources'] = level_0_results[1]

    # Level 1: set_performance_benchmarks, preprocess_data, choose_strategy_approach
    async def run_set_performance_benchmarks():
        # Call the async version of set_performance_benchmarks with results from dependencies
        return await set_performance_benchmarks_async(results['define_strategy_objective'])

    async def run_preprocess_data():
        # Call the async version of preprocess_data with results from dependencies
        return await preprocess_data_async(results['select_data_sources'])

    async def run_choose_strategy_approach():
        # Call the async version of choose_strategy_approach with results from dependencies
        return await choose_strategy_approach_async(results['define_strategy_objective'])

    # Run level 1 nodes in parallel
    level_1_results = await asyncio.gather(run_set_performance_benchmarks(), run_preprocess_data(), run_choose_strategy_approach())
    results['set_performance_benchmarks'] = level_1_results[0]
    results['preprocess_data'] = level_1_results[1]
    results['choose_strategy_approach'] = level_1_results[2]

    # Level 2: calculate_position_sizing, develop_entry_rules, implement_slippage_model, develop_exit_rules, build_risk_rules, set_backtest_parameters
    async def run_calculate_position_sizing():
        # Call the async version of calculate_position_sizing with results from dependencies
        return await calculate_position_sizing_async(results['set_performance_benchmarks'])

    async def run_develop_entry_rules():
        # Call the async version of develop_entry_rules with results from dependencies
        return await develop_entry_rules_async(results['choose_strategy_approach'], results['preprocess_data'])

    async def run_implement_slippage_model():
        # Call the async version of implement_slippage_model with results from dependencies
        return await implement_slippage_model_async(results['preprocess_data'])

    async def run_develop_exit_rules():
        # Call the async version of develop_exit_rules with results from dependencies
        return await develop_exit_rules_async(results['choose_strategy_approach'], results['preprocess_data'])

    async def run_build_risk_rules():
        # Call the async version of build_risk_rules with results from dependencies
        return await build_risk_rules_async(results['set_performance_benchmarks'])

    async def run_set_backtest_parameters():
        # Call the async version of set_backtest_parameters with results from dependencies
        return await set_backtest_parameters_async(results['preprocess_data'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_calculate_position_sizing(), run_develop_entry_rules(), run_implement_slippage_model(), run_develop_exit_rules(), run_build_risk_rules(), run_set_backtest_parameters())
    results['calculate_position_sizing'] = level_2_results[0]
    results['develop_entry_rules'] = level_2_results[1]
    results['implement_slippage_model'] = level_2_results[2]
    results['develop_exit_rules'] = level_2_results[3]
    results['build_risk_rules'] = level_2_results[4]
    results['set_backtest_parameters'] = level_2_results[5]

    # Level 3: execute_in_sample_backtest
    async def run_execute_in_sample_backtest():
        # Call the async version of execute_in_sample_backtest with results from dependencies
        return await execute_in_sample_backtest_async(results['develop_entry_rules'], results['develop_exit_rules'], results['calculate_position_sizing'], results['implement_slippage_model'], results['build_risk_rules'], results['set_backtest_parameters'])

    # Run level 3 nodes in parallel
    results['execute_in_sample_backtest'] = await run_execute_in_sample_backtest()

    # Level 4: analyze_backtest_results
    async def run_analyze_backtest_results():
        # Call the async version of analyze_backtest_results with results from dependencies
        return await analyze_backtest_results_async(results['execute_in_sample_backtest'], results['set_performance_benchmarks'])

    # Run level 4 nodes in parallel
    results['analyze_backtest_results'] = await run_analyze_backtest_results()

    # Level 5: optimize_parameters
    async def run_optimize_parameters():
        # Call the async version of optimize_parameters with results from dependencies
        return await optimize_parameters_async(results['analyze_backtest_results'])

    # Run level 5 nodes in parallel
    results['optimize_parameters'] = await run_optimize_parameters()

    # Level 6: validate_out_of_sample, deploy_automated_backtest
    async def run_validate_out_of_sample():
        # Call the async version of validate_out_of_sample with results from dependencies
        return await validate_out_of_sample_async(results['optimize_parameters'], results['set_backtest_parameters'])

    async def run_deploy_automated_backtest():
        # Call the async version of deploy_automated_backtest with results from dependencies
        return await deploy_automated_backtest_async(results['optimize_parameters'], results['implement_slippage_model'], results['set_backtest_parameters'])

    # Run level 6 nodes in parallel
    level_6_results = await asyncio.gather(run_validate_out_of_sample(), run_deploy_automated_backtest())
    results['validate_out_of_sample'] = level_6_results[0]
    results['deploy_automated_backtest'] = level_6_results[1]

    # Level 7: compile_strategy_documentation
    async def run_compile_strategy_documentation():
        # Call the async version of compile_strategy_documentation with results from dependencies
        return await compile_strategy_documentation_async(results['develop_entry_rules'], results['develop_exit_rules'], results['calculate_position_sizing'], results['build_risk_rules'], results['validate_out_of_sample'])

    # Run level 7 nodes in parallel
    results['compile_strategy_documentation'] = await run_compile_strategy_documentation()

    # Level 8: generate_strategy_presentation
    async def run_generate_strategy_presentation():
        # Call the async version of generate_strategy_presentation with results from dependencies
        return await generate_strategy_presentation_async(results['compile_strategy_documentation'], results['validate_out_of_sample'])

    # Run level 8 nodes in parallel
    results['generate_strategy_presentation'] = await run_generate_strategy_presentation()

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
