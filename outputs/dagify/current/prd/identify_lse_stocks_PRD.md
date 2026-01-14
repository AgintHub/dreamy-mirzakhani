# identify_lse_stocks PRD

## Description
Generates a comprehensive, protocol‑aware catalogue of London Stock Exchange (LSE) equities to be queried. The output includes precise data‑feed details—protocol, latency expectations, and geographically proximate data‑centre information—to enable downstream nodes to select the optimal ingestion pathway and satisfy strict performance SLAs.


## Conceptual Info

Defines a protocol-aware catalogue of LSE equities with per-symbol feed details to drive optimal ingestion routing and SLA compliance downstream.

## Docstring

### Summary
Return a structured catalogue of LSE equities with per-symbol data feed protocol, latency, and datacenter requirements.

### Returns

List[Dict[str, Union[str, int]]]: A list of records, each describing an LSE symbol with fields: symbol, market, protocol, latency_ms, datacenter, and tier.

### Raises

- ValueError: Raised if the catalogue cannot be retrieved or a symbol entry is malformed.
- RuntimeError: Raised if downstream data feeds or data centers are unavailable.

### Examples

```python
>>> identify_lse_stocks()
[{"symbol": "LON-AAL", "market": 1, "protocol": "REST", "latency_ms": 120, "datacenter": "London-West", "tier": 1}]
```

```python
>>> identify_lse_stocks()
[{"symbol": "LON-LLOY", "market": 1, "protocol": "FIX", "latency_ms": 65, "datacenter": "London-East", "tier": 2}]
```
