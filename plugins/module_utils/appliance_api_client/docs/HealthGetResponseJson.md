# HealthGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health** | [**SchemasHealth**](SchemasHealth.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.health_get_response_json import HealthGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of HealthGetResponseJson from a JSON string
health_get_response_json_instance = HealthGetResponseJson.from_json(json)
# print the JSON string representation of the object
print HealthGetResponseJson.to_json()

# convert the object into a dict
health_get_response_json_dict = health_get_response_json_instance.to_dict()
# create an instance of HealthGetResponseJson from a dict
health_get_response_json_form_dict = health_get_response_json.from_dict(health_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


