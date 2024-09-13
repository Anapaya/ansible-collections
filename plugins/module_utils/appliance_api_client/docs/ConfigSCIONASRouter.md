# ConfigSCIONASRouter

The configuration for the SCION router service. The address configures where the router is exposed. AS internal hosts send SCION data plane traffic to this address for forwarding over the local SCION interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the service is enabled. | 
**internal_interface** | **str** | The address of internal SCION interface of the router. The address must be specified as host:port. If the port is 0 it will be automatically allocated. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas_router import ConfigSCIONASRouter

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASRouter from a JSON string
config_scionas_router_instance = ConfigSCIONASRouter.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASRouter.to_json()

# convert the object into a dict
config_scionas_router_dict = config_scionas_router_instance.to_dict()
# create an instance of ConfigSCIONASRouter from a dict
config_scionas_router_form_dict = config_scionas_router.from_dict(config_scionas_router_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


