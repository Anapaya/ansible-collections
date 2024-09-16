# ScionTunnelingPrefixesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | An action for prefixes. | 
**prefixes** | **List[str]** | A list of IP prefixes. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_prefixes_filter import ScionTunnelingPrefixesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingPrefixesFilter from a JSON string
scion_tunneling_prefixes_filter_instance = ScionTunnelingPrefixesFilter.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingPrefixesFilter.to_json()

# convert the object into a dict
scion_tunneling_prefixes_filter_dict = scion_tunneling_prefixes_filter_instance.to_dict()
# create an instance of ScionTunnelingPrefixesFilter from a dict
scion_tunneling_prefixes_filter_form_dict = scion_tunneling_prefixes_filter.from_dict(scion_tunneling_prefixes_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


