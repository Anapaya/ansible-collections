# AnnounceFilterMatchesPrefixData

The entry in the announce filter matches at least one prefix that is announced in a domain. While it is not invalid to have an announce filter entry that does not match anything, it is certainly curious. This health check is meant to help operators identify such cases. This only applies to the entries with action `accept`.  If `count` is zero, the status is `notice`. Otherwise, the status is `passing`. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain the announce filter entry is part of.  | 
**prefixes** | **List[str]** | The prefixes that the filter entry is configured with. This is not the set of prefixes that are actually matched by the entry.  | 
**count** | **int** | The number of prefixes that are matched by the accept filter entry. We count unique prefixes, so if a prefix is matched multiple times, or is announced by multiple remotes, it only counts once. Two overlapping prefixes are counted individually.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.announce_filter_matches_prefix_data import AnnounceFilterMatchesPrefixData

# TODO update the JSON string below
json = "{}"
# create an instance of AnnounceFilterMatchesPrefixData from a JSON string
announce_filter_matches_prefix_data_instance = AnnounceFilterMatchesPrefixData.from_json(json)
# print the JSON string representation of the object
print AnnounceFilterMatchesPrefixData.to_json()

# convert the object into a dict
announce_filter_matches_prefix_data_dict = announce_filter_matches_prefix_data_instance.to_dict()
# create an instance of AnnounceFilterMatchesPrefixData from a dict
announce_filter_matches_prefix_data_form_dict = announce_filter_matches_prefix_data.from_dict(announce_filter_matches_prefix_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


