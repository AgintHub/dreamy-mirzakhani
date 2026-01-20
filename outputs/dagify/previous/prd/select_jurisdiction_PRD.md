# select_jurisdiction PRD

## Description
Choose optimal fund domicile


## Conceptual Info

This node evaluates the fund’s strategic objectives to recommend a domicile jurisdiction that best aligns with legal, tax, and operational considerations. It returns the selected jurisdiction name along with a balanced pros‑and‑cons list to inform downstream decisions such as legal entity selection.

## Docstring

### Summary
Selects the most suitable fund domicile based on the fund’s objectives, returning the jurisdiction name and a concise pros/cons list.

### Parameters

- **objectives** (List[str]): Concise bullet list of the fund’s primary business objectives, including investment purpose, competitive edge, and long‑term vision.
- **investment_purpose** (str): Description of the investment purpose derived from the objectives.
- **competitive_edge** (str): Description of the competitive edge identified from the objectives.
- **long_term_vision** (str): Description of the long‑term vision derived from the objectives.

### Returns

Dict[str, Any]: Dictionary with keys 'selected_jurisdiction' (str), 'pros' (List[str]), and 'cons' (List[str]).

### Raises

- ValueError: Raised if any of the objective inputs are missing or empty.

### Examples

```python
>>> select_jurisdiction(

...     objectives=[

...         "Generate alpha via multi‑strategy equity", 

...         "Leverage low regulatory friction", 

...         "Maintain investor confidentiality"

...     ],
...     investment_purpose="Long‑term capital appreciation via diversified equity strategies",
...     competitive_edge="Low tax burden and flexible legal framework",
...     long_term_vision="Become a leading independent multi‑strategy fund in the Americas"

>>> )
{
  "selected_jurisdiction": "Cayman Islands",
  "pros": ["Low corporate tax and no capital gains tax", "Strong confidentiality protections and established fund industry"],
  "cons": ["Perception of regulatory laxity may deter certain investors", "Limited local banking infrastructure requires offshore arrangements"]
}
```

```python
>>> select_jurisdiction(

...     objectives=["Global macro trading with high leverage"],

...     investment_purpose="Capture macro opportunities worldwide",
...     competitive_edge="Ability to deploy large leverage efficiently",
...     long_term_vision="Scale to $10B AUM within 5 years"

>>> )
{
  "selected_jurisdiction": "Delaware, USA",
  "pros": ["Well‑established legal framework for LLCs", "Access to U.S. capital markets and regulatory clarity"],
  "cons": ["Higher U.S. tax obligations for foreign investors", "More stringent reporting and disclosure requirements"]
}
```
