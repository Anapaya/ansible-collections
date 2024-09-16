# ConfigInterfacesVlan

List of VLAN interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_ra** | **bool** | Whether to accept the route advertisements for the corresponding interface. (This is currently supported only for the interfaces that are using the Linux driver.) | [optional] [default to False]
**addresses** | **List[str]** | The addresses configured on this interface. Each address must be a valid IP prefix in CIDR notation. | [optional] 
**gateway** | [**ConfigInterfacesVlanGateway**](ConfigInterfacesVlanGateway.md) |  | [optional] 
**id** | **int** | The VLAN ID of the VLAN interface. It ranges between 0 and 4095. | 
**link** | **str** | The name of the physical interface used for this VLAN. | 
**mac** | **str** | The MAC address to use on this interface. It is of the form &#x60;XX:XX:XX:XX:XX:XX&#x60;. | [optional] 
**mtu** | **int** | The MTU (Maximum Transmission Unit) to be used on this interface. | [optional] [default to 1500]
**name** | **str** | The name of the network interface. | 
**neighbors** | [**List[ConfigInterfacesVlanNeighbor]**](ConfigInterfacesVlanNeighbor.md) | The static neighbors configured on this network interface. | [optional] 
**routes** | [**List[ConfigInterfacesVlanRoute]**](ConfigInterfacesVlanRoute.md) | The routes which are configured on this network interface. | [optional] 
**rx_queue_size** | **int** | The number of descriptors in the receive queue. (This option is currently supported only for VPP interfaces.) | [optional] [default to 1024]
**tx_queue_size** | **int** | The number of descriptors in the transmit queue. (This is currently supported only for VPP interfaces.) | [optional] [default to 1024]
**vrrp** | [**List[ConfigInterfacesVlanVrrp]**](ConfigInterfacesVlanVrrp.md) | The VRRP (Virtual Router Redundancy Protocol) configurations for this interface. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_vlan import ConfigInterfacesVlan

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesVlan from a JSON string
config_interfaces_vlan_instance = ConfigInterfacesVlan.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesVlan.to_json()

# convert the object into a dict
config_interfaces_vlan_dict = config_interfaces_vlan_instance.to_dict()
# create an instance of ConfigInterfacesVlan from a dict
config_interfaces_vlan_form_dict = config_interfaces_vlan.from_dict(config_interfaces_vlan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


