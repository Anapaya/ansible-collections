# ScionInterfaceEndpoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd_as** | **str** |  | 
**address** | **str** | The IP address of this endpoint of the SCION interface. | 
**interface_id** | **int** | The ID of the Interface. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_interface_endpoint import ScionInterfaceEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ScionInterfaceEndpoint from a JSON string
scion_interface_endpoint_instance = ScionInterfaceEndpoint.from_json(json)
# print the JSON string representation of the object
print ScionInterfaceEndpoint.to_json()

# convert the object into a dict
scion_interface_endpoint_dict = scion_interface_endpoint_instance.to_dict()
# create an instance of ScionInterfaceEndpoint from a dict
scion_interface_endpoint_form_dict = scion_interface_endpoint.from_dict(scion_interface_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


