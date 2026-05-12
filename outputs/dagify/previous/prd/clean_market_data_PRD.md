# clean_market_data PRD

## Description
Clean raw market data.


## Conceptual Info


          This node cleans raw market data to remove duplicates and adjust for missing timestamps and corporate actions.

        

## Docstring

### Summary

            Cleans market data by removing duplicates and adjusting for missing timestamps and corporate actions.
            
            Parameters
            ----------
            collect_market_data : str
              Path to the output CSV file
            data_csv : List[str]
              List of asset symbols retrieved
            timestamp_fill_type : str
              Type of timestamp filling used (e.g., forward-fill)
            
            Returns
            -------
            cleaned_market_data : List[str]
              List of cleaned CSV files containing market data
            duplicate_bar_count : int
              Number of duplicate bars removed
            
            Raises
            ------
            ValueError
              If input data is null or empty
            
            Examples
            --------
            >>> clean_market_data(collect_market_data='file.csv', data_csv=['asset1', 'asset2'], timestamp_fill_type='forward-fill')
            {'cleaned_market_data': ['cleaned_asset1.csv', 'cleaned_asset2.csv'], 'duplicate_bar_count': 5}
          

### Parameters

- **collect_market_data** (str): Path to the output CSV file
- **data_csv** (List[str]): List of asset symbols retrieved
- **timestamp_fill_type** (str): Type of timestamp filling used (e.g., forward-fill)

### Returns

Dict[str, str]: List of cleaned CSV files containing market data

### Raises

- ValueError: If input data is null or empty

### Examples

```python
>>> clean_market_data(collect_market_data='file.csv', data_csv=['asset1', 'asset2'], timestamp_fill_type='forward-fill')
{'cleaned_market_data': ['cleaned_asset1.csv', 'cleaned_asset2.csv'], 'duplicate_bar_count': 5}
```
