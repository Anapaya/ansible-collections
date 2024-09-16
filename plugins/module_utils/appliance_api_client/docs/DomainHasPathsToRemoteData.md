# DomainHasPathsToRemoteData

Indicates the number of paths a domain has to a remote ISD-AS. If the domain has multiple ISD-AS, it could be that a path is not available for a certain ISD-AS pair, nonetheless, this is a condition to be aware of. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of the routing domain.  | 
**local_isd_as** | **str** | The local ISD-AS in the domain.  | 
**remote_isd_as** | **str** | The remote ISD-AS in the domain.  | 
**paths** | **int** | The number of alive paths between the local and remote ISD-AS.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_has_paths_to_remote_data import DomainHasPathsToRemoteData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainHasPathsToRemoteData from a JSON string
domain_has_paths_to_remote_data_instance = DomainHasPathsToRemoteData.from_json(json)
# print the JSON string representation of the object
print DomainHasPathsToRemoteData.to_json()

# convert the object into a dict
domain_has_paths_to_remote_data_dict = domain_has_paths_to_remote_data_instance.to_dict()
# create an instance of DomainHasPathsToRemoteData from a dict
domain_has_paths_to_remote_data_form_dict = domain_has_paths_to_remote_data.from_dict(domain_has_paths_to_remote_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


