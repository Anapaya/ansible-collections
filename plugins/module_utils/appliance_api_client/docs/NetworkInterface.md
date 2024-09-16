# NetworkInterface

Network interface summary.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the interface. | 
**mtu** | **int** | MTU of the interface. | 
**state** | **str** | State of the interface. Either up or down. Unknown means that the interface is in inconsistent state.  | 
**driver** | **str** | Which networking stack (linux, vpp) the interface is part of. | 
**addresses** | **List[str]** | IP addresses configured on the interface. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.network_interface import NetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterface from a JSON string
network_interface_instance = NetworkInterface.from_json(json)
# print the JSON string representation of the object
print NetworkInterface.to_json()

# convert the object into a dict
network_interface_dict = network_interface_instance.to_dict()
# create an instance of NetworkInterface from a dict
network_interface_form_dict = network_interface.from_dict(network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


