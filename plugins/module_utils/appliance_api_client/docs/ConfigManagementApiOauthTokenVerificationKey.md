# ConfigManagementApiOauthTokenVerificationKey

The list of JWT verification keys specified as a JSON Web Key Set (JWKS).  Each key set contains keys that enable the appliance to verify tokens signed by corresponding private keys. This is useful in case the appliance API is not accessed via a browser where the OAuth redirect flow of the identity provider likely does not work. This list is not required if the browser redirect flow is enough for your use case.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the key. Must be unique among all keys. | [optional] 
**jwks_url** | **str** | URL for fetching JSON Web Key Sets. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth_token_verification_key import ConfigManagementApiOauthTokenVerificationKey

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiOauthTokenVerificationKey from a JSON string
config_management_api_oauth_token_verification_key_instance = ConfigManagementApiOauthTokenVerificationKey.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiOauthTokenVerificationKey.to_json()

# convert the object into a dict
config_management_api_oauth_token_verification_key_dict = config_management_api_oauth_token_verification_key_instance.to_dict()
# create an instance of ConfigManagementApiOauthTokenVerificationKey from a dict
config_management_api_oauth_token_verification_key_form_dict = config_management_api_oauth_token_verification_key.from_dict(config_management_api_oauth_token_verification_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


