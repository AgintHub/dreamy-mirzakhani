# determine_vendor_involvement PRD

## Description
Determines vendor involvement for each stage in the operations workflow based on responsible parties.


## Conceptual Info

This shim function determines vendor involvement for each stage in the operations workflow based on responsible parties.

## Docstring

### Summary
Determines vendor involvement for each stage in the operations workflow based on responsible parties.

### Parameters

- **responsible_parties** (str): List of responsible parties for each stage in the operations workflow.

### Returns

List[bool]: List of boolean flags indicating vendor involvement for each stage.

### Raises

- ValueError: When input validation fails.
- TypeError: When input types are incorrect.

### Examples

```python
>>> determine_vendor_involvement(responsible_parties=['In-house', 'Prime Broker', 'In-house'])
[False, True, False]
```

```python
>>> determine_vendor_involvement(responsible_parties=['Vendor', 'Vendor', 'In-house'])
[True, True, False]
```
