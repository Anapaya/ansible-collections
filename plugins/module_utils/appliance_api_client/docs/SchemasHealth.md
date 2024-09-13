# SchemasHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HealthStatus**](HealthStatus.md) |  | 
**checks** | [**List[HealthCheck]**](HealthCheck.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.schemas_health import SchemasHealth

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasHealth from a JSON string
schemas_health_instance = SchemasHealth.from_json(json)
# print the JSON string representation of the object
print SchemasHealth.to_json()

# convert the object into a dict
schemas_health_dict = schemas_health_instance.to_dict()
# create an instance of SchemasHealth from a dict
schemas_health_form_dict = schemas_health.from_dict(schemas_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


