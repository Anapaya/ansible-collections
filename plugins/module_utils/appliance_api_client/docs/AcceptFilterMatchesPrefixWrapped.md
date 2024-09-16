# AcceptFilterMatchesPrefixWrapped


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.accept_filter_matches_prefix_wrapped import AcceptFilterMatchesPrefixWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptFilterMatchesPrefixWrapped from a JSON string
accept_filter_matches_prefix_wrapped_instance = AcceptFilterMatchesPrefixWrapped.from_json(json)
# print the JSON string representation of the object
print AcceptFilterMatchesPrefixWrapped.to_json()

# convert the object into a dict
accept_filter_matches_prefix_wrapped_dict = accept_filter_matches_prefix_wrapped_instance.to_dict()
# create an instance of AcceptFilterMatchesPrefixWrapped from a dict
accept_filter_matches_prefix_wrapped_form_dict = accept_filter_matches_prefix_wrapped.from_dict(accept_filter_matches_prefix_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


