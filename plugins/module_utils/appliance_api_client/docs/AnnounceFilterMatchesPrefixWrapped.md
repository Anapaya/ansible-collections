# AnnounceFilterMatchesPrefixWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.announce_filter_matches_prefix_wrapped import AnnounceFilterMatchesPrefixWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of AnnounceFilterMatchesPrefixWrapped from a JSON string
announce_filter_matches_prefix_wrapped_instance = AnnounceFilterMatchesPrefixWrapped.from_json(json)
# print the JSON string representation of the object
print AnnounceFilterMatchesPrefixWrapped.to_json()

# convert the object into a dict
announce_filter_matches_prefix_wrapped_dict = announce_filter_matches_prefix_wrapped_instance.to_dict()
# create an instance of AnnounceFilterMatchesPrefixWrapped from a dict
announce_filter_matches_prefix_wrapped_form_dict = announce_filter_matches_prefix_wrapped.from_dict(announce_filter_matches_prefix_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


