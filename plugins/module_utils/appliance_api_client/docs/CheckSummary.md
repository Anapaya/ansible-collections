# CheckSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Name of the service. | [optional] 
**name** | **str** | Name of health check. | 
**status** | [**Status**](Status.md) |  | 
**data** | **Dict[str, object]** |  | 
**reason** | **str** | Reason for check failure. | [optional] 
**detail** | **str** | Additional information. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.check_summary import CheckSummary

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSummary from a JSON string
check_summary_instance = CheckSummary.from_json(json)
# print the JSON string representation of the object
print CheckSummary.to_json()

# convert the object into a dict
check_summary_dict = check_summary_instance.to_dict()
# create an instance of CheckSummary from a dict
check_summary_form_dict = check_summary.from_dict(check_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


