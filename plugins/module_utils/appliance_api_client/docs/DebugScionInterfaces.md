# DebugScionInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | [**List[DebugScionInterface]**](DebugScionInterface.md) |  | 
**sibling_interfaces** | [**List[DebugScionSiblingInterface]**](DebugScionSiblingInterface.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.debug_scion_interfaces import DebugScionInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of DebugScionInterfaces from a JSON string
debug_scion_interfaces_instance = DebugScionInterfaces.from_json(json)
# print the JSON string representation of the object
print DebugScionInterfaces.to_json()

# convert the object into a dict
debug_scion_interfaces_dict = debug_scion_interfaces_instance.to_dict()
# create an instance of DebugScionInterfaces from a dict
debug_scion_interfaces_form_dict = debug_scion_interfaces.from_dict(debug_scion_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


