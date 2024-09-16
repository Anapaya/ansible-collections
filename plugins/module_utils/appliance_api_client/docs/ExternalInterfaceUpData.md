# ExternalInterfaceUpData

The external interface to a neighboring SCION AS is up.  If the interface is configured with BFD enabled, the health check reports up if the BFD session is up. If BFD is not enabled, the health check always reports up. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_isd_as** | **str** |  | 
**local_address** | **str** | The local underaly UDP address. | 
**local_interface** | **int** | The local interface identifier. | 
**remote_isd_as** | **str** |  | 
**remote_address** | **str** | The remote underaly UDP address. | 
**remote_interface** | **int** | The remote interface identifier. | 
**relationship** | [**LinkRelationship**](LinkRelationship.md) |  | 
**state** | [**LinkState**](LinkState.md) |  | 
**bfd_enabled** | **bool** | Whether BFD is enabled on the interface. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.external_interface_up_data import ExternalInterfaceUpData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalInterfaceUpData from a JSON string
external_interface_up_data_instance = ExternalInterfaceUpData.from_json(json)
# print the JSON string representation of the object
print ExternalInterfaceUpData.to_json()

# convert the object into a dict
external_interface_up_data_dict = external_interface_up_data_instance.to_dict()
# create an instance of ExternalInterfaceUpData from a dict
external_interface_up_data_form_dict = external_interface_up_data.from_dict(external_interface_up_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


