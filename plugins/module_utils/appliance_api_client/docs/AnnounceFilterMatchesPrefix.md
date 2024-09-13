# AnnounceFilterMatchesPrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AnnounceFilterMatchesPrefixData**](AnnounceFilterMatchesPrefixData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.announce_filter_matches_prefix import AnnounceFilterMatchesPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of AnnounceFilterMatchesPrefix from a JSON string
announce_filter_matches_prefix_instance = AnnounceFilterMatchesPrefix.from_json(json)
# print the JSON string representation of the object
print AnnounceFilterMatchesPrefix.to_json()

# convert the object into a dict
announce_filter_matches_prefix_dict = announce_filter_matches_prefix_instance.to_dict()
# create an instance of AnnounceFilterMatchesPrefix from a dict
announce_filter_matches_prefix_form_dict = announce_filter_matches_prefix.from_dict(announce_filter_matches_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


