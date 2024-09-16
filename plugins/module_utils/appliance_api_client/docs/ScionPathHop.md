# ScionPathHop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ifid** | **int** | ID of the SCION interface. | 
**isd_as** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_path_hop import ScionPathHop

# TODO update the JSON string below
json = "{}"
# create an instance of ScionPathHop from a JSON string
scion_path_hop_instance = ScionPathHop.from_json(json)
# print the JSON string representation of the object
print ScionPathHop.to_json()

# convert the object into a dict
scion_path_hop_dict = scion_path_hop_instance.to_dict()
# create an instance of ScionPathHop from a dict
scion_path_hop_form_dict = scion_path_hop.from_dict(scion_path_hop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


