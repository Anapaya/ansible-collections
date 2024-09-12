# DebugScionSiblingInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mtu** | **int** | The MTU of the SCION interface | 
**relationship** | [**LinkRelationship**](LinkRelationship.md) |  | 
**remote_isd_as** | **str** |  | 
**local_isd_as** | **str** |  | 
**local_interface_id** | **int** | The ID of the Interface. | 
**next_hop_address** | **str** | The IP and port of the next hop. | 

## Example

```python
from openapi_client.models.debug_scion_sibling_interface import DebugScionSiblingInterface

# TODO update the JSON string below
json = "{}"
# create an instance of DebugScionSiblingInterface from a JSON string
debug_scion_sibling_interface_instance = DebugScionSiblingInterface.from_json(json)
# print the JSON string representation of the object
print DebugScionSiblingInterface.to_json()

# convert the object into a dict
debug_scion_sibling_interface_dict = debug_scion_sibling_interface_instance.to_dict()
# create an instance of DebugScionSiblingInterface from a dict
debug_scion_sibling_interface_form_dict = debug_scion_sibling_interface.from_dict(debug_scion_sibling_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


