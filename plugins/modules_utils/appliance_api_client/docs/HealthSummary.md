# HealthSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | 
**checks** | [**List[CheckSummary]**](CheckSummary.md) | List of health checks. | 

## Example

```python
from openapi_client.models.health_summary import HealthSummary

# TODO update the JSON string below
json = "{}"
# create an instance of HealthSummary from a JSON string
health_summary_instance = HealthSummary.from_json(json)
# print the JSON string representation of the object
print HealthSummary.to_json()

# convert the object into a dict
health_summary_dict = health_summary_instance.to_dict()
# create an instance of HealthSummary from a dict
health_summary_form_dict = health_summary.from_dict(health_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


