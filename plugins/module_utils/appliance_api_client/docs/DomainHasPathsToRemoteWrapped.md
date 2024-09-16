# DomainHasPathsToRemoteWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_has_paths_to_remote_wrapped import DomainHasPathsToRemoteWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of DomainHasPathsToRemoteWrapped from a JSON string
domain_has_paths_to_remote_wrapped_instance = DomainHasPathsToRemoteWrapped.from_json(json)
# print the JSON string representation of the object
print DomainHasPathsToRemoteWrapped.to_json()

# convert the object into a dict
domain_has_paths_to_remote_wrapped_dict = domain_has_paths_to_remote_wrapped_instance.to_dict()
# create an instance of DomainHasPathsToRemoteWrapped from a dict
domain_has_paths_to_remote_wrapped_form_dict = domain_has_paths_to_remote_wrapped.from_dict(domain_has_paths_to_remote_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


