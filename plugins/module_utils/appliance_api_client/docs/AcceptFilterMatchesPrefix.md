# AcceptFilterMatchesPrefix

Check data for an explanation of this health check. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AcceptFilterMatchesPrefixData**](AcceptFilterMatchesPrefixData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.accept_filter_matches_prefix import AcceptFilterMatchesPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptFilterMatchesPrefix from a JSON string
accept_filter_matches_prefix_instance = AcceptFilterMatchesPrefix.from_json(json)
# print the JSON string representation of the object
print AcceptFilterMatchesPrefix.to_json()

# convert the object into a dict
accept_filter_matches_prefix_dict = accept_filter_matches_prefix_instance.to_dict()
# create an instance of AcceptFilterMatchesPrefix from a dict
accept_filter_matches_prefix_form_dict = accept_filter_matches_prefix.from_dict(accept_filter_matches_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


