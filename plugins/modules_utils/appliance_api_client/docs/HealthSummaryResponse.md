# HealthSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health** | [**HealthSummary**](HealthSummary.md) |  | 

## Example

```python
from openapi_client.models.health_summary_response import HealthSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HealthSummaryResponse from a JSON string
health_summary_response_instance = HealthSummaryResponse.from_json(json)
# print the JSON string representation of the object
print HealthSummaryResponse.to_json()

# convert the object into a dict
health_summary_response_dict = health_summary_response_instance.to_dict()
# create an instance of HealthSummaryResponse from a dict
health_summary_response_form_dict = health_summary_response.from_dict(health_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


