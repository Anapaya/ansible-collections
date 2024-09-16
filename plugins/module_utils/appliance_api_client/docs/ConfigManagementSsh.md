# ConfigManagementSsh

Configuration for SSH access to the Anapaya appliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_password_login** | **bool** | Whether password login is enabled for SSH access to the Anapaya appliance. | [optional] [default to False]
**users** | [**List[ConfigManagementSshUser]**](ConfigManagementSshUser.md) | Users with SSH access to the Anapaya appliance. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_ssh import ConfigManagementSsh

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementSsh from a JSON string
config_management_ssh_instance = ConfigManagementSsh.from_json(json)
# print the JSON string representation of the object
print ConfigManagementSsh.to_json()

# convert the object into a dict
config_management_ssh_dict = config_management_ssh_instance.to_dict()
# create an instance of ConfigManagementSsh from a dict
config_management_ssh_form_dict = config_management_ssh.from_dict(config_management_ssh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


