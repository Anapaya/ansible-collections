# ConfigManagementRemoteRepositoryCloudsmith

The configuration data for the cloudsmith repository. This section is provided only when the remote repository is cloudsmith.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The token used to access the remote cloudsmith repository. It must be of the form &lt;api_key&gt;#&lt;entitlement_token&gt; | [optional] 
**url** | **str** | The url which is used to access the cloudsmith repository. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_remote_repository_cloudsmith import ConfigManagementRemoteRepositoryCloudsmith

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementRemoteRepositoryCloudsmith from a JSON string
config_management_remote_repository_cloudsmith_instance = ConfigManagementRemoteRepositoryCloudsmith.from_json(json)
# print the JSON string representation of the object
print ConfigManagementRemoteRepositoryCloudsmith.to_json()

# convert the object into a dict
config_management_remote_repository_cloudsmith_dict = config_management_remote_repository_cloudsmith_instance.to_dict()
# create an instance of ConfigManagementRemoteRepositoryCloudsmith from a dict
config_management_remote_repository_cloudsmith_form_dict = config_management_remote_repository_cloudsmith.from_dict(config_management_remote_repository_cloudsmith_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


