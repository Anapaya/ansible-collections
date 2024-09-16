# PhysicalInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**pcie_bdf** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**driver** | **str** |  | 
**num_vfs** | **int** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.physical_interface import PhysicalInterface

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalInterface from a JSON string
physical_interface_instance = PhysicalInterface.from_json(json)
# print the JSON string representation of the object
print PhysicalInterface.to_json()

# convert the object into a dict
physical_interface_dict = physical_interface_instance.to_dict()
# create an instance of PhysicalInterface from a dict
physical_interface_form_dict = physical_interface.from_dict(physical_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


