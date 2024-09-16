# ConfigManagementApiOauthIdentityProvider

The id of the identity provider.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_auth_url** | **str** | The base URL for the identity provider. | [optional] 
**client_id** | **str** | The client ID for this identity provider. | [optional] 
**client_secret** | **str** | The client secret for this identity provider. | [optional] 
**id** | **str** | The identifier of the provider. Must be unique among all providers. | [optional] 
**metadata_url** | **str** | The URL for fetching the open ID configuration. | [optional] 
**tenant_id** | **str** | The tenant ID for Azure AD | [optional] 
**type** | **str** | The type of the provider. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth_identity_provider import ConfigManagementApiOauthIdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiOauthIdentityProvider from a JSON string
config_management_api_oauth_identity_provider_instance = ConfigManagementApiOauthIdentityProvider.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiOauthIdentityProvider.to_json()

# convert the object into a dict
config_management_api_oauth_identity_provider_dict = config_management_api_oauth_identity_provider_instance.to_dict()
# create an instance of ConfigManagementApiOauthIdentityProvider from a dict
config_management_api_oauth_identity_provider_form_dict = config_management_api_oauth_identity_provider.from_dict(config_management_api_oauth_identity_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


