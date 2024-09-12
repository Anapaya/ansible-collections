# ConfigInterfacesVirtualFunctionGateway

The gateway for the network interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_gateway** | **str** | The gateway address for the IPv4 networking stack. Note that there must only be one IPv4 gateway configured across all the interfaces. | [optional] 
**ipv6_gateway** | **str** | The gateway address for the IPv6 networking stack. Note that there must only be one IPv6 gateway configured across all the interfaces. | [optional] 

## Example

```python
from openapi_client.models.config_interfaces_virtual_function_gateway import ConfigInterfacesVirtualFunctionGateway

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesVirtualFunctionGateway from a JSON string
config_interfaces_virtual_function_gateway_instance = ConfigInterfacesVirtualFunctionGateway.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesVirtualFunctionGateway.to_json()

# convert the object into a dict
config_interfaces_virtual_function_gateway_dict = config_interfaces_virtual_function_gateway_instance.to_dict()
# create an instance of ConfigInterfacesVirtualFunctionGateway from a dict
config_interfaces_virtual_function_gateway_form_dict = config_interfaces_virtual_function_gateway.from_dict(config_interfaces_virtual_function_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


