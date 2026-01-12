from ._test_app_functionality.validate_integrate_features_input import validate_integrate_features_input
from ._test_app_functionality.setup_test_environment import setup_test_environment
from ._test_app_functionality.execute_unit_tests import execute_unit_tests
from ._test_app_functionality.execute_integration_tests import execute_integration_tests
from ._test_app_functionality.execute_selenium_ui_tests import execute_selenium_ui_tests
from ._test_app_functionality.calculate_total_test_cases import calculate_total_test_cases
from ._test_app_functionality.calculate_passed_test_cases import calculate_passed_test_cases
from ._test_app_functionality.identify_defects import identify_defects
from ._test_app_functionality.prepare_jmeter_config import prepare_jmeter_config
from ._test_app_functionality.execute_stress_tests import execute_stress_tests
from ._test_app_functionality.evaluate_stress_test_results import evaluate_stress_test_results
from ._test_app_functionality.collect_performance_metrics import collect_performance_metrics
from ._test_app_functionality.generate_performance_summary import generate_performance_summary
from ._test_app_functionality.aggregate_test_logs import aggregate_test_logs
from ._test_app_functionality.generate_recommendations import generate_recommendations
from ._test_app_functionality.cleanup_test_environment import cleanup_test_environment

from pydantic import BaseModel, Field
from typing import List


class IntegrateFeaturesOutput(BaseModel):
    """Pydantic model for integrate_features node outputs."""
    sample_id: str = (
        Field(..., description="Identifier of the audio sample being processed")
    )
    sample_identified: bool = (
        Field(..., description = (
            "Whether the sample has been successfully identified")
        )
    )
    identified_tracks_count: int = (
        Field(..., description = (
            "Number of candidate tracks returned by identification")
        )
    )
    musician_ids: List[str] = (
        Field(..., description = (
            "List of unique musician identifiers extracted from identified tracks")
        )
    )
    musician_count: int = (
        Field(..., description="Total number of musicians in the list")
    )
    playlist_id: str = (
        Field(..., description="Identifier of the generated playlist")
    )
    playlist_created: bool = (
        Field(..., description="Whether the playlist was successfully created")
    )
    playlist_track_count: int = (
        Field(..., description="Number of tracks in the created playlist")
    )
    error_message: str = (
        Field(..., description = (
            "Error message if any operation failed, \u043d\u0430\u0448\u0438\u043c otherwise")
        )
    )
    snackbar_visible: bool = (
        Field(..., description = (
            "Whether a snackbar notification is currently visible")
        )
    )
    snackbar_message: str = (
        Field(..., description="Content of the snackbar notification")
    )
    loading_state: str = (
        Field(..., description = (
            "Current loading state of the UI (e.g., idle, loading, success, error)")
        )
    )


class TestAppFunctionalityOutput(BaseModel):
    """Pydantic model for test_app_functionality node outputs."""
    test_passed: bool = (
        Field(..., description="Overall pass/fail status of the test suite.")
    )
    total_test_cases: int = (
        Field(..., description="Total number of test cases executed.")
    )
    passed_test_cases: int = (
        Field(..., description="Number of test cases that passed.")
    )
    failed_test_cases: int = (
        Field(..., description="Number of test cases that failed.")
    )
    defect_ids: List[str] = (
        Field(..., description = (
            "List of defect identifiers reported during testing.")
        )
    )
    defect_count: int = Field(..., description="Total number of defects found.")
    stress_test_passed: bool = (
        Field(..., description="Whether the stress test (e.g., JMeter) passed.")
    )
    performance_metric_summary: str = (
        Field(..., description = (
            "Summary of performance metrics such as latency, throughput.")
        )
    )
    log_file_path: str = (
        Field(..., description="File path to the aggregated logs.")
    )
    recommendation_summary: str = (
        Field(..., description="High-level recommendations for optimization.")
    )


def test_app_functionality(integrate_features_input: IntegrateFeaturesOutput, **kwargs) -> TestAppFunctionalityOutput:
    """
    Executes a multi-faceted testing regimen on the music sample identifier app,
    validating its functionality and performance.

    Parameters
    ----------
    integrate_features_output : dict
        Output from the 'integrate_features' node, containing the integrated
        features of the application.

    Returns
    -------
    dict
        A dictionary containing the test results, including pass/fail
        status, test case counts, defect information, stress test results,
        performance metrics, log file path, and recommendations.

    Raises
    ------
    ValueError
        If the input from 'integrate_features' is invalid or missing
        required fields.
    RuntimeError
        If any of the testing processes (e.g., Selenium WebDriver, Pytest,
        JMeter) encounter execution errors.

    Examples
    --------
    >>> test_app_functionality(integrate_features_output={'sample_id': '123',
    'sample_identified': True, ...})
    {'test_passed': True, 'total_test_cases': 10, 'passed_test_cases': 9,
    'failed_test_cases': 1, 'defect_ids': ['DEF-1'], 'defect_count': 1,
    'stress_test_passed': True, 'performance_metric_summary': 'Average latency:
    200ms', 'log_file_path': '/logs/test.log', 'recommendation_summary':
    'Optimize database queries'}

    """
    validate_integrate_features_input(input_data=integrate_features_input)
    
    test_environment = setup_test_environment(app_state=integrate_features_input)
    
    unit_test_results = execute_unit_tests(environment=test_environment)
    integration_test_results = execute_integration_tests(environment=test_environment, app_features=integrate_features_input)
    ui_test_results = execute_selenium_ui_tests(environment=test_environment, app_state=integrate_features_input)
    
    total_cases: int = calculate_total_test_cases(unit_results=unit_test_results, integration_results=integration_test_results, ui_results=ui_test_results)
    passed_cases: int = calculate_passed_test_cases(unit_results=unit_test_results, integration_results=integration_test_results, ui_results=ui_test_results)
    failed_cases: int = total_cases - passed_cases
    
    defects: List[str] = identify_defects(unit_results=unit_test_results, integration_results=integration_test_results, ui_results=ui_test_results)
    defect_count: int = len(defects)
    
    stress_test_config = prepare_jmeter_config(app_features=integrate_features_input)
    stress_results = execute_stress_tests(config=stress_test_config)
    stress_passed: bool = evaluate_stress_test_results(results=stress_results)
    
    performance_metrics = collect_performance_metrics(stress_results=stress_results, functional_results=[unit_test_results, integration_test_results, ui_test_results])
    performance_summary: str = generate_performance_summary(metrics=performance_metrics)
    
    log_path: str = aggregate_test_logs(unit_logs=unit_test_results.get('logs'), integration_logs=integration_test_results.get('logs'), ui_logs=ui_test_results.get('logs'), stress_logs=stress_results.get('logs'))
    
    recommendations: str = generate_recommendations(defects=defects, performance_metrics=performance_metrics, test_results=[unit_test_results, integration_test_results, ui_test_results])
    
    overall_passed: bool = failed_cases == 0 and stress_passed
    
    cleanup_test_environment(environment=test_environment)
    
    return TestAppFunctionalityOutput(
        test_passed=overall_passed,
        total_test_cases=total_cases,
        passed_test_cases=passed_cases,
        failed_test_cases=failed_cases,
        defect_ids=defects,
        defect_count=defect_count,
        stress_test_passed=stress_passed,
        performance_metric_summary=performance_summary,
        log_file_path=log_path,
        recommendation_summary=recommendations
    )