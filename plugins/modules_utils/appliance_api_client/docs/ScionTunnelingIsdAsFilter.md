# ScionTunnelingIsdAsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | An action for ISD-AS filtering. | 
**isd_as** | **str** |  | 

## Example

```python
from openapi_client.models.scion_tunneling_isd_as_filter import ScionTunnelingIsdAsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingIsdAsFilter from a JSON string
scion_tunneling_isd_as_filter_instance = ScionTunnelingIsdAsFilter.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingIsdAsFilter.to_json()

# convert the object into a dict
scion_tunneling_isd_as_filter_dict = scion_tunneling_isd_as_filter_instance.to_dict()
# create an instance of ScionTunnelingIsdAsFilter from a dict
scion_tunneling_isd_as_filter_form_dict = scion_tunneling_isd_as_filter.from_dict(scion_tunneling_isd_as_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


