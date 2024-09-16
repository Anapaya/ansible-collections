# ConfigScionTunnelingRemote

List of remote ISD-ASes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description or Comment on the remote. | [optional] 
**isd_as** | **str** | The ISD-AS of the remote. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_remote import ConfigScionTunnelingRemote

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingRemote from a JSON string
config_scion_tunneling_remote_instance = ConfigScionTunnelingRemote.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingRemote.to_json()

# convert the object into a dict
config_scion_tunneling_remote_dict = config_scion_tunneling_remote_instance.to_dict()
# create an instance of ConfigScionTunnelingRemote from a dict
config_scion_tunneling_remote_form_dict = config_scion_tunneling_remote.from_dict(config_scion_tunneling_remote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


