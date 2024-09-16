# ConfigManagementApiListener

List of management API listeners which define where the API is exposed.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | An address that is used to expose the Anapaya appliance management API. This can be either a combination of an IP address and a fixed port, or a SCION address. The address must be specified as ip:port for IPv4, [ip]:port for IPv6 and [ISD-AS,ip]:port for SCION. | [optional] 
**description** | **str** | Description, or comment, for the listener. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_api_listener import ConfigManagementApiListener

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiListener from a JSON string
config_management_api_listener_instance = ConfigManagementApiListener.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiListener.to_json()

# convert the object into a dict
config_management_api_listener_dict = config_management_api_listener_instance.to_dict()
# create an instance of ConfigManagementApiListener from a dict
config_management_api_listener_form_dict = config_management_api_listener.from_dict(config_management_api_listener_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


