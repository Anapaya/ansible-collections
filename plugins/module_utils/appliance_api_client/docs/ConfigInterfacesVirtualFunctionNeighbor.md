# ConfigInterfacesVirtualFunctionNeighbor

List of neighbors configured on this interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address. | 
**comment** | **str** | An optional human-readable string to comment on this neighbor. | [optional] 
**mac** | **str** | The MAC address corresponding to the address. It is of the form &#x60;XX:XX:XX:XX:XX:XX&#x60;. | [optional] 
**sequence_id** | **int** | The sequence id determines the order of the neighbor entries. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_virtual_function_neighbor import ConfigInterfacesVirtualFunctionNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesVirtualFunctionNeighbor from a JSON string
config_interfaces_virtual_function_neighbor_instance = ConfigInterfacesVirtualFunctionNeighbor.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesVirtualFunctionNeighbor.to_json()

# convert the object into a dict
config_interfaces_virtual_function_neighbor_dict = config_interfaces_virtual_function_neighbor_instance.to_dict()
# create an instance of ConfigInterfacesVirtualFunctionNeighbor from a dict
config_interfaces_virtual_function_neighbor_form_dict = config_interfaces_virtual_function_neighbor.from_dict(config_interfaces_virtual_function_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


