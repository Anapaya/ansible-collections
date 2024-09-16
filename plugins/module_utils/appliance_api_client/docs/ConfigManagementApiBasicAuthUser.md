# ConfigManagementApiBasicAuthUser

List of user credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password_hashed** | **str** | The user password hashed based on the hash algorithm indicated by the prefix in the string. The string takes the following form based on the Unix crypt function:  $id[$param&#x3D;value(,param&#x3D;value)*][$salt[$hash]]  Supported hash functions are:  - $2y$: bcrypt  The &#39;appliance-cli&#39; or the &#39;htpasswd&#39; tool can be used to create a password hash. E.g., &#39;appliance-cli crypto kdf hash&#39; or &#39;htpasswd -nB admin&#39; prompts for a password.  | 
**username** | **str** | Name of the user. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_api_basic_auth_user import ConfigManagementApiBasicAuthUser

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiBasicAuthUser from a JSON string
config_management_api_basic_auth_user_instance = ConfigManagementApiBasicAuthUser.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiBasicAuthUser.to_json()

# convert the object into a dict
config_management_api_basic_auth_user_dict = config_management_api_basic_auth_user_instance.to_dict()
# create an instance of ConfigManagementApiBasicAuthUser from a dict
config_management_api_basic_auth_user_form_dict = config_management_api_basic_auth_user.from_dict(config_management_api_basic_auth_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


