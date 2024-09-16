# ConfigManagementRemoteRepository

Remote repository configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudsmith** | [**ConfigManagementRemoteRepositoryCloudsmith**](ConfigManagementRemoteRepositoryCloudsmith.md) |  | [optional] 
**repository_type** | **str** | The type of remote repository used for storing the software packages. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_remote_repository import ConfigManagementRemoteRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementRemoteRepository from a JSON string
config_management_remote_repository_instance = ConfigManagementRemoteRepository.from_json(json)
# print the JSON string representation of the object
print ConfigManagementRemoteRepository.to_json()

# convert the object into a dict
config_management_remote_repository_dict = config_management_remote_repository_instance.to_dict()
# create an instance of ConfigManagementRemoteRepository from a dict
config_management_remote_repository_form_dict = config_management_remote_repository.from_dict(config_management_remote_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


