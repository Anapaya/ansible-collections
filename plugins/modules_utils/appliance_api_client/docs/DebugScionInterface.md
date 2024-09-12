# DebugScionInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | [**ScionInterfaceEndpoint**](ScionInterfaceEndpoint.md) |  | 
**remote** | [**ScionInterfaceEndpoint**](ScionInterfaceEndpoint.md) |  | 
**relationship** | [**LinkRelationship**](LinkRelationship.md) |  | 
**mtu** | **int** | The MTU of the SCION interface | 
**state** | [**LinkState**](LinkState.md) |  | 

## Example

```python
from openapi_client.models.debug_scion_interface import DebugScionInterface

# TODO update the JSON string below
json = "{}"
# create an instance of DebugScionInterface from a JSON string
debug_scion_interface_instance = DebugScionInterface.from_json(json)
# print the JSON string representation of the object
print DebugScionInterface.to_json()

# convert the object into a dict
debug_scion_interface_dict = debug_scion_interface_instance.to_dict()
# create an instance of DebugScionInterface from a dict
debug_scion_interface_form_dict = debug_scion_interface.from_dict(debug_scion_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


