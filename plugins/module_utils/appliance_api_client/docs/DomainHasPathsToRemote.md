# DomainHasPathsToRemote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DomainHasPathsToRemoteData**](DomainHasPathsToRemoteData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_has_paths_to_remote import DomainHasPathsToRemote

# TODO update the JSON string below
json = "{}"
# create an instance of DomainHasPathsToRemote from a JSON string
domain_has_paths_to_remote_instance = DomainHasPathsToRemote.from_json(json)
# print the JSON string representation of the object
print DomainHasPathsToRemote.to_json()

# convert the object into a dict
domain_has_paths_to_remote_dict = domain_has_paths_to_remote_instance.to_dict()
# create an instance of DomainHasPathsToRemote from a dict
domain_has_paths_to_remote_form_dict = domain_has_paths_to_remote.from_dict(domain_has_paths_to_remote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


