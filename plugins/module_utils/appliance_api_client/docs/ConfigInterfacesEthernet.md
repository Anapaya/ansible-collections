# ConfigInterfacesEthernet

List of ethernet interfaces.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_ra** | **bool** | Whether to accept the route advertisements for the corresponding interface. (This is currently supported only for the interfaces that are using the Linux driver.) | [optional] [default to False]
**addresses** | **List[str]** | The addresses configured on this interface. Each address must be a valid IP prefix in CIDR notation. | [optional] 
**driver** | **str** | The driver which should be used for the interface. | [optional] 
**gateway** | [**ConfigInterfacesEthernetGateway**](ConfigInterfacesEthernetGateway.md) |  | [optional] 
**mac** | **str** | The MAC address to use on this interface. It is of the form &#x60;XX:XX:XX:XX:XX:XX&#x60;. | [optional] 
**mtu** | **int** | The MTU (Maximum Transmission Unit) to be used on this interface. | [optional] [default to 1500]
**name** | **str** | The name of the network interface. | 
**neighbors** | [**List[ConfigInterfacesEthernetNeighbor]**](ConfigInterfacesEthernetNeighbor.md) | The static neighbors configured on this network interface. | [optional] 
**routes** | [**List[ConfigInterfacesEthernetRoute]**](ConfigInterfacesEthernetRoute.md) | The routes which are configured on this network interface. | [optional] 
**rx_queue_size** | **int** | The number of descriptors in the receive queue. (This option is currently supported only for VPP interfaces.) | [optional] [default to 1024]
**tx_queue_size** | **int** | The number of descriptors in the transmit queue. (This is currently supported only for VPP interfaces.) | [optional] [default to 1024]
**vpp** | [**ConfigInterfacesEthernetVpp**](ConfigInterfacesEthernetVpp.md) |  | [optional] 
**vrrp** | [**List[ConfigInterfacesEthernetVrrp]**](ConfigInterfacesEthernetVrrp.md) | The VRRP (Virtual Router Redundancy Protocol) configurations for this interface. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_ethernet import ConfigInterfacesEthernet

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesEthernet from a JSON string
config_interfaces_ethernet_instance = ConfigInterfacesEthernet.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesEthernet.to_json()

# convert the object into a dict
config_interfaces_ethernet_dict = config_interfaces_ethernet_instance.to_dict()
# create an instance of ConfigInterfacesEthernet from a dict
config_interfaces_ethernet_form_dict = config_interfaces_ethernet.from_dict(config_interfaces_ethernet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


