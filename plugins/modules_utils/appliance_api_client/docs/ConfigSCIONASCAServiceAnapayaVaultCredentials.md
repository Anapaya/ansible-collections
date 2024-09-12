# ConfigSCIONASCAServiceAnapayaVaultCredentials

The necessary credentials to be logged into the Anapaya Vault backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The role ID used to authenticate with the Vault backend via the AppRole Authentication Method. See https://www.vaultproject.io/docs/auth/approle for more details. | [optional] 
**secret_id** | **str** | The secret ID used to authenticate with the Vault backend via the AppRole Authentication Method. See https://www.vaultproject.io/docs/auth/approle for more details. | [optional] 

## Example

```python
from openapi_client.models.config_scionasca_service_anapaya_vault_credentials import ConfigSCIONASCAServiceAnapayaVaultCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCAServiceAnapayaVaultCredentials from a JSON string
config_scionasca_service_anapaya_vault_credentials_instance = ConfigSCIONASCAServiceAnapayaVaultCredentials.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCAServiceAnapayaVaultCredentials.to_json()

# convert the object into a dict
config_scionasca_service_anapaya_vault_credentials_dict = config_scionasca_service_anapaya_vault_credentials_instance.to_dict()
# create an instance of ConfigSCIONASCAServiceAnapayaVaultCredentials from a dict
config_scionasca_service_anapaya_vault_credentials_form_dict = config_scionasca_service_anapaya_vault_credentials.from_dict(config_scionasca_service_anapaya_vault_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


