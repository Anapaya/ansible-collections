# ConfigManagementSshUserSshKey

List of SSH keys that are authorized to access the Anapaya appliance, as a specific user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description or comment for the key. | [optional] 
**key** | **str** | The SSH public key of the user. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_ssh_user_ssh_key import ConfigManagementSshUserSshKey

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementSshUserSshKey from a JSON string
config_management_ssh_user_ssh_key_instance = ConfigManagementSshUserSshKey.from_json(json)
# print the JSON string representation of the object
print ConfigManagementSshUserSshKey.to_json()

# convert the object into a dict
config_management_ssh_user_ssh_key_dict = config_management_ssh_user_ssh_key_instance.to_dict()
# create an instance of ConfigManagementSshUserSshKey from a dict
config_management_ssh_user_ssh_key_form_dict = config_management_ssh_user_ssh_key.from_dict(config_management_ssh_user_ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


