# ConfigSystemResources

Anapaya appliance system resources configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_limits** | [**List[ConfigSystemResourcesServiceLimit]**](ConfigSystemResourcesServiceLimit.md) | Configuration for per service resource limits. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_resources import ConfigSystemResources

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemResources from a JSON string
config_system_resources_instance = ConfigSystemResources.from_json(json)
# print the JSON string representation of the object
print ConfigSystemResources.to_json()

# convert the object into a dict
config_system_resources_dict = config_system_resources_instance.to_dict()
# create an instance of ConfigSystemResources from a dict
config_system_resources_form_dict = config_system_resources.from_dict(config_system_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


