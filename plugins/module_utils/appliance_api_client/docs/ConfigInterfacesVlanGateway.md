# ConfigInterfacesVlanGateway

The gateway for the network interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_gateway** | **str** | The gateway address for the IPv4 networking stack. Note that there must only be one IPv4 gateway configured across all the interfaces. | [optional] 
**ipv6_gateway** | **str** | The gateway address for the IPv6 networking stack. Note that there must only be one IPv6 gateway configured across all the interfaces. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_vlan_gateway import ConfigInterfacesVlanGateway

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesVlanGateway from a JSON string
config_interfaces_vlan_gateway_instance = ConfigInterfacesVlanGateway.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesVlanGateway.to_json()

# convert the object into a dict
config_interfaces_vlan_gateway_dict = config_interfaces_vlan_gateway_instance.to_dict()
# create an instance of ConfigInterfacesVlanGateway from a dict
config_interfaces_vlan_gateway_form_dict = config_interfaces_vlan_gateway.from_dict(config_interfaces_vlan_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


