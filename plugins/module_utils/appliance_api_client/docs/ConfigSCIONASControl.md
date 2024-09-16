# ConfigSCIONASControl

The configuration for the SCION control service. The address configures where the control service is exposed. Clients connect to this address to request control plane data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the control service. The address must be specified as host:port. If the port is 0 it will be automatically allocated. | [optional] 
**enabled** | **bool** | Whether the service is enabled. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas_control import ConfigSCIONASControl

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASControl from a JSON string
config_scionas_control_instance = ConfigSCIONASControl.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASControl.to_json()

# convert the object into a dict
config_scionas_control_dict = config_scionas_control_instance.to_dict()
# create an instance of ConfigSCIONASControl from a dict
config_scionas_control_form_dict = config_scionas_control.from_dict(config_scionas_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


