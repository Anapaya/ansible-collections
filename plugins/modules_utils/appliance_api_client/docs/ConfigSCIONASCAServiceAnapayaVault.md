# ConfigSCIONASCAServiceAnapayaVault

The configuration data of the Anapaya SCION CPPKI CA service. This section is provided only when the CA service type is Anapaya Vault, i.e., is operated by Anapaya.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The list of addresses where the Anapaya Vault backend can be reached. This list must be non-empty. | [optional] 
**credentials** | [**ConfigSCIONASCAServiceAnapayaVaultCredentials**](ConfigSCIONASCAServiceAnapayaVaultCredentials.md) |  | [optional] 
**validation** | [**ConfigSCIONASCAServiceAnapayaVaultValidation**](ConfigSCIONASCAServiceAnapayaVaultValidation.md) |  | [optional] 

## Example

```python
from openapi_client.models.config_scionasca_service_anapaya_vault import ConfigSCIONASCAServiceAnapayaVault

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCAServiceAnapayaVault from a JSON string
config_scionasca_service_anapaya_vault_instance = ConfigSCIONASCAServiceAnapayaVault.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCAServiceAnapayaVault.to_json()

# convert the object into a dict
config_scionasca_service_anapaya_vault_dict = config_scionasca_service_anapaya_vault_instance.to_dict()
# create an instance of ConfigSCIONASCAServiceAnapayaVault from a dict
config_scionasca_service_anapaya_vault_form_dict = config_scionasca_service_anapaya_vault.from_dict(config_scionasca_service_anapaya_vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


