# ConfigSystem

The necessary configuration data for the system of the Anapaya appliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns** | [**ConfigSystemDns**](ConfigSystemDns.md) |  | [optional] 
**kernel** | [**ConfigSystemKernel**](ConfigSystemKernel.md) |  | [optional] 
**ntp** | [**ConfigSystemNtp**](ConfigSystemNtp.md) |  | [optional] 
**resources** | [**ConfigSystemResources**](ConfigSystemResources.md) |  | [optional] 
**vpp** | [**ConfigSystemVpp**](ConfigSystemVpp.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system import ConfigSystem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystem from a JSON string
config_system_instance = ConfigSystem.from_json(json)
# print the JSON string representation of the object
print ConfigSystem.to_json()

# convert the object into a dict
config_system_dict = config_system_instance.to_dict()
# create an instance of ConfigSystem from a dict
config_system_form_dict = config_system.from_dict(config_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


