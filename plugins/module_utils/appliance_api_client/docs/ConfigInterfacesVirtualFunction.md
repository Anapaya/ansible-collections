# ConfigInterfacesVirtualFunction

List of virtual function interfaces.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_ra** | **bool** | Whether to accept the route advertisements for the corresponding interface. (This is currently supported only for the interfaces that are using the Linux driver.) | [optional] [default to False]
**addresses** | **List[str]** | The addresses configured on this interface. Each address must be a valid IP prefix in CIDR notation. | [optional] 
**gateway** | [**ConfigInterfacesVirtualFunctionGateway**](ConfigInterfacesVirtualFunctionGateway.md) |  | [optional] 
**link** | **str** | The name of the network interface that is used as the parent on which the virtual function will be created. | 
**mac** | **str** | The MAC address to use on this interface. It is of the form &#x60;XX:XX:XX:XX:XX:XX&#x60;. | [optional] 
**mtu** | **int** | The MTU (Maximum Transmission Unit) to be used on this interface. | [optional] [default to 1500]
**name** | **str** | The name of the network interface. | 
**neighbors** | [**List[ConfigInterfacesVirtualFunctionNeighbor]**](ConfigInterfacesVirtualFunctionNeighbor.md) | The static neighbors configured on this network interface. | [optional] 
**routes** | [**List[ConfigInterfacesVirtualFunctionRoute]**](ConfigInterfacesVirtualFunctionRoute.md) | The routes which are configured on this network interface. | [optional] 
**rx_queue_size** | **int** | The number of descriptors in the receive queue. (This option is currently supported only for VPP interfaces.) | [optional] [default to 1024]
**tx_queue_size** | **int** | The number of descriptors in the transmit queue. (This is currently supported only for VPP interfaces.) | [optional] [default to 1024]
**vrrp** | [**List[ConfigInterfacesVirtualFunctionVrrp]**](ConfigInterfacesVirtualFunctionVrrp.md) | The VRRP (Virtual Router Redundancy Protocol) configurations for this interface. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_virtual_function import ConfigInterfacesVirtualFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesVirtualFunction from a JSON string
config_interfaces_virtual_function_instance = ConfigInterfacesVirtualFunction.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesVirtualFunction.to_json()

# convert the object into a dict
config_interfaces_virtual_function_dict = config_interfaces_virtual_function_instance.to_dict()
# create an instance of ConfigInterfacesVirtualFunction from a dict
config_interfaces_virtual_function_form_dict = config_interfaces_virtual_function.from_dict(config_interfaces_virtual_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


