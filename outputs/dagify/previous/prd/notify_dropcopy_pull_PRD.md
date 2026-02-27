# notify_dropcopy_pull PRD

## Description
Communicates to stakeholders the successful retrieval, integrity verification, and processing of the dropcopy dataset using secure OAuth authentication to ensure authorized and auditable notification delivery.


## Conceptual Info

This node securely notifies relevant stakeholders that a dropcopy dataset has been successfully pulled, its integrity verified, and processing completed without errors. It uses OAuth authentication to ensure secure and authorized notification delivery, including detailed metadata for traceability and auditability.

## Docstring

### Summary
Notify stakeholders via secure OAuth-authenticated channels that the dropcopy dataset has been successfully retrieved, integrity-verified, and processed without errors, including metadata for traceability.

### Parameters

- **dropcopy_id** (str): The unique identifier for the dropcopy dataset involved in the notification.
- **verification_hash** (str): The cryptographic hash value used to verify the dataset's integrity.
- **verification_timestamp** (str): ISO 8601 timestamp recording when the integrity verification was performed.
- **is_verified** (bool): Boolean flag indicating whether the dropcopy passed integrity verification.
- **processing_time_seconds** (float): Total number of seconds spent processing the dropcopy.
- **stakeholders_notified** (List[str]): List of stakeholder identifiers (e.g., email addresses) to which notifications are sent.

### Returns

dict: A dictionary containing notification status, message, timestamp, stakeholders notified, dropcopy metadata, verification details, processing time, and an error message if any.

### Raises

- NotificationError: Raised if notification delivery fails due to network or authentication issues.
- ValueError: Raised if input parameters are invalid or missing.

### Examples

```python
>>> result = notify_dropcopy_pull(
...     dropcopy_id='dropcopy_20240615',
...     verification_hash='3a5f789acdbe...',
...     verification_timestamp='2024-06-15T12:00:00Z',
...     is_verified=True,
...     processing_time_seconds=45.7,
...     stakeholders_notified=['tradingdesk@example.com', 'compliance@example.com']
>>> )
>>> print(result['notification_status'])
>>> print(result['notification_message'])
['sent', 'Dropcopy dropcopy_20240615 successfully pulled, verified at 2024-06-15T12:00:00Z, and processed in 45.7 seconds. Integrity verification passed. Notifications sent to 2 stakeholders.']
```
