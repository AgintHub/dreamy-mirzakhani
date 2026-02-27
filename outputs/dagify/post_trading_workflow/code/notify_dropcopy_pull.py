from pydantic import BaseModel, Field
from typing import List


class VerifyDropcopyIntegrityOutput(BaseModel):
    """Pydantic model for verify_dropcopy_integrity node outputs."""
    is_integrity_valid: bool = (
        Field(..., description="Boolean indicating whether the dropcopy integrity verification passed successfully")
    )
    validation_timestamp: str = (
        Field(..., description="ISO 8601 timestamp when the integrity verification was performed")
    )
    validation_method: str = (
        Field(..., description="Name of the cryptographic method or algorithm used for the integrity verification")
    )
    details_message: str = (
        Field(..., description="Additional information or notes related to the verification process, including error messages if verification failed")
    )


class NotifyDropcopyPullOutput(BaseModel):
    """Pydantic model for notify_dropcopy_pull node outputs."""
    notification_status: str = (
        Field(..., description="Status of the notification delivery (e.g., 'sent', 'failed').")
    )
    notification_message: str = (
        Field(..., description="The content of the notification sent to stakeholders.")
    )
    notification_timestamp: str = (
        Field(..., description="ISO 8601 timestamp when the notification was sent.")
    )
    stakeholders_notified: List[str] = (
        Field(..., description="List of stakeholder identifiers (e.g., email addresses) who received the notification.")
    )
    dropcopy_id: str = (
        Field(..., description="Unique identifier of the dropcopy dataset.")
    )
    verification_hash: str = (
        Field(..., description="Cryptographic hash value used to verify the dropcopy integrity.")
    )
    verification_timestamp: str = (
        Field(..., description="ISO 8601 timestamp when the dropcopy integrity verification was performed.")
    )
    is_verified: bool = (
        Field(..., description="True if the dropcopy integrity verification succeeded; false otherwise.")
    )
    processing_time_seconds: float = (
        Field(..., description="Total time in seconds spent processing the dropcopy.")
    )
    error_message: str = (
        Field(..., description="Error details if the notification or verification failed; empty string otherwise.")
    )


def notify_dropcopy_pull(verify_dropcopy_integrity_input: VerifyDropcopyIntegrityOutput, **kwargs) -> NotifyDropcopyPullOutput:
    """
    Notify stakeholders via secure OAuth-authenticated channels that the
    dropcopy dataset has been successfully retrieved, integrity-verified, and
    processed without errors, including metadata for traceability.

    Parameters
    ----------
    dropcopy_id : str
        The unique identifier for the dropcopy dataset involved in the
        notification.
    verification_hash : str
        The cryptographic hash value used to verify the dataset's integrity.
    verification_timestamp : str
        ISO 8601 timestamp recording when the integrity verification was
        performed.
    is_verified : bool
        Boolean flag indicating whether the dropcopy passed integrity
        verification.
    processing_time_seconds : float
        Total number of seconds spent processing the dropcopy.
    stakeholders_notified : List[str]
        List of stakeholder identifiers (e.g., email addresses) to which
        notifications are sent.

    Returns
    -------
    dict
        A dictionary containing notification status, message, timestamp,
        stakeholders notified, dropcopy metadata, verification details,
        processing time, and an error message if any.

    Raises
    ------
    NotificationError
        Raised if notification delivery fails due to network or
        authentication issues.
    ValueError
        Raised if input parameters are invalid or missing.

    Examples
    --------
    >>> result = notify_dropcopy_pull(
    ...     dropcopy_id='dropcopy_20240615',
    ...     verification_hash='3a5f789acdbe...',
    ...     verification_timestamp='2024-06-15T12:00:00Z',
    ...     is_verified=True,
    ...     processing_time_seconds=45.7,
    ...     stakeholders_notified=['tradingdesk@example.com',
    'compliance@example.com']
    >>> )
    >>> print(result['notification_status'])
    >>> print(result['notification_message'])
    ['sent', 'Dropcopy dropcopy_20240615 successfully pulled, verified at
    2024-06-15T12:00:00Z, and processed in 45.7 seconds. Integrity verification
    passed. Notifications sent to 2 stakeholders.']

    """
    return NotifyDropcopyPullOutput(
        notification_status="",
        notification_message="",
        notification_timestamp="",
        stakeholders_notified=[],
        dropcopy_id="",
        verification_hash="",
        verification_timestamp="",
        is_verified=False,
        processing_time_seconds=0.0,
        error_message="",
    )