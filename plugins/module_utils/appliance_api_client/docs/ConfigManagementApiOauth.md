# ConfigManagementApiOauth

Open authorization (OAuth) configuration that can authorize users who want to access the Anapaya appliance management API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the feature is enabled. | [optional] [default to False]
**identity_providers** | [**List[ConfigManagementApiOauthIdentityProvider]**](ConfigManagementApiOauthIdentityProvider.md) | The identity providers. Currently only one is supported. | [optional] 
**roles** | [**List[ConfigManagementApiOauthRole]**](ConfigManagementApiOauthRole.md) | Roles configuration used for OAuth. | [optional] 
**token_verification_keys** | [**List[ConfigManagementApiOauthTokenVerificationKey]**](ConfigManagementApiOauthTokenVerificationKey.md) | Keys to verify JWTs. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth import ConfigManagementApiOauth

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiOauth from a JSON string
config_management_api_oauth_instance = ConfigManagementApiOauth.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiOauth.to_json()

# convert the object into a dict
config_management_api_oauth_dict = config_management_api_oauth_instance.to_dict()
# create an instance of ConfigManagementApiOauth from a dict
config_management_api_oauth_form_dict = config_management_api_oauth.from_dict(config_management_api_oauth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


