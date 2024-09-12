# ConfigScionTunnelingEndpointAllowedInterfaces

List of configurations for allowed interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | **List[int]** | List of allowed interfaces for this SCION AS | [optional] 
**isd_as** | **str** | The SCION AS where the list of allowed interfaces applies. Packets to this IP-in-SCION tunnel endpoint in this SCION AS will only arrive on the listed interfaces. | [optional] 

## Example

```python
from openapi_client.models.config_scion_tunneling_endpoint_allowed_interfaces import ConfigScionTunnelingEndpointAllowedInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingEndpointAllowedInterfaces from a JSON string
config_scion_tunneling_endpoint_allowed_interfaces_instance = ConfigScionTunnelingEndpointAllowedInterfaces.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingEndpointAllowedInterfaces.to_json()

# convert the object into a dict
config_scion_tunneling_endpoint_allowed_interfaces_dict = config_scion_tunneling_endpoint_allowed_interfaces_instance.to_dict()
# create an instance of ConfigScionTunnelingEndpointAllowedInterfaces from a dict
config_scion_tunneling_endpoint_allowed_interfaces_form_dict = config_scion_tunneling_endpoint_allowed_interfaces.from_dict(config_scion_tunneling_endpoint_allowed_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


