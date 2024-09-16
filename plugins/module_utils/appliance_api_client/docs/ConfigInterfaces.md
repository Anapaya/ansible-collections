# ConfigInterfaces

Top-level configuration and state for interfaces.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonds** | [**List[ConfigInterfacesBond]**](ConfigInterfacesBond.md) | Top-level configuration and state for the bond interfaces. | [optional] 
**ethernets** | [**List[ConfigInterfacesEthernet]**](ConfigInterfacesEthernet.md) | Top-level configuration and state for ethernet interfaces. | [optional] 
**loopbacks** | [**List[ConfigInterfacesLoopback]**](ConfigInterfacesLoopback.md) | Top-level configuration and state for loopback interfaces. | [optional] 
**virtual_functions** | [**List[ConfigInterfacesVirtualFunction]**](ConfigInterfacesVirtualFunction.md) | Top-level configuration and state for VF interfaces. | [optional] 
**vlans** | [**List[ConfigInterfacesVlan]**](ConfigInterfacesVlan.md) | Top-level configuration and state for VLAN interfaces. | [optional] 
**wireguards** | [**List[ConfigInterfacesWireguard]**](ConfigInterfacesWireguard.md) | Top-level configuration and state for Wireguard interfaces. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces import ConfigInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfaces from a JSON string
config_interfaces_instance = ConfigInterfaces.from_json(json)
# print the JSON string representation of the object
print ConfigInterfaces.to_json()

# convert the object into a dict
config_interfaces_dict = config_interfaces_instance.to_dict()
# create an instance of ConfigInterfaces from a dict
config_interfaces_form_dict = config_interfaces.from_dict(config_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


