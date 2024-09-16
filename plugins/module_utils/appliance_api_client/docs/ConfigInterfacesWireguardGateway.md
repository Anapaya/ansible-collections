# ConfigInterfacesWireguardGateway

The gateway for the network interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_gateway** | **str** | The gateway address for the IPv4 networking stack. Note that there must only be one IPv4 gateway configured across all the interfaces. | [optional] 
**ipv6_gateway** | **str** | The gateway address for the IPv6 networking stack. Note that there must only be one IPv6 gateway configured across all the interfaces. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_wireguard_gateway import ConfigInterfacesWireguardGateway

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesWireguardGateway from a JSON string
config_interfaces_wireguard_gateway_instance = ConfigInterfacesWireguardGateway.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesWireguardGateway.to_json()

# convert the object into a dict
config_interfaces_wireguard_gateway_dict = config_interfaces_wireguard_gateway_instance.to_dict()
# create an instance of ConfigInterfacesWireguardGateway from a dict
config_interfaces_wireguard_gateway_form_dict = config_interfaces_wireguard_gateway.from_dict(config_interfaces_wireguard_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


