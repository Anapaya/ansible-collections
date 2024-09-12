# Check


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of health check. | 
**status** | [**Status**](Status.md) |  | 
**data** | **Dict[str, object]** |  | 
**reason** | **str** | Reason for check failure. | [optional] 
**detail** | **str** | Additional information. | [optional] 

## Example

```python
from openapi_client.models.check import Check

# TODO update the JSON string below
json = "{}"
# create an instance of Check from a JSON string
check_instance = Check.from_json(json)
# print the JSON string representation of the object
print Check.to_json()

# convert the object into a dict
check_dict = check_instance.to_dict()
# create an instance of Check from a dict
check_form_dict = check.from_dict(check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


