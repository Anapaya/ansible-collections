# ConfigManagementSshUser

List of users that are authorized to access the Anapaya appliance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_keys** | [**List[ConfigManagementSshUserSshKey]**](ConfigManagementSshUserSshKey.md) | List of SSH keys that are authorized for the given user. This list is authoritative and overwrites the list of existing SSH keys in the user&#39;s authorized_keys file. | [optional] 
**username** | **str** | The unix username of the user. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_ssh_user import ConfigManagementSshUser

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementSshUser from a JSON string
config_management_ssh_user_instance = ConfigManagementSshUser.from_json(json)
# print the JSON string representation of the object
print ConfigManagementSshUser.to_json()

# convert the object into a dict
config_management_ssh_user_dict = config_management_ssh_user_instance.to_dict()
# create an instance of ConfigManagementSshUser from a dict
config_management_ssh_user_form_dict = config_management_ssh_user.from_dict(config_management_ssh_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


