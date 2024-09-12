# SiblingInterfaceUpData

The connectivity to a SCION interface that is configured on a sibling appliance is up.  If the interface is configured with BFD enabled, the health check reports up if the BFD session is up. If BFD is not enabled, the health check always reports up. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_isd_as** | **str** |  | 
**local_interface** | **int** | The local interface identifier on the Sibling appliance. | 
**internal_address** | **str** | The internal interface address of the Sibling appliance. | 
**remote_isd_as** | **str** |  | 
**relationship** | [**LinkRelationship**](LinkRelationship.md) |  | 
**state** | [**LinkState**](LinkState.md) |  | 
**bfd_enabled** | **bool** | Whether BFD is enabled to that Sibling appliance. | 

## Example

```python
from openapi_client.models.sibling_interface_up_data import SiblingInterfaceUpData

# TODO update the JSON string below
json = "{}"
# create an instance of SiblingInterfaceUpData from a JSON string
sibling_interface_up_data_instance = SiblingInterfaceUpData.from_json(json)
# print the JSON string representation of the object
print SiblingInterfaceUpData.to_json()

# convert the object into a dict
sibling_interface_up_data_dict = sibling_interface_up_data_instance.to_dict()
# create an instance of SiblingInterfaceUpData from a dict
sibling_interface_up_data_form_dict = sibling_interface_up_data.from_dict(sibling_interface_up_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


