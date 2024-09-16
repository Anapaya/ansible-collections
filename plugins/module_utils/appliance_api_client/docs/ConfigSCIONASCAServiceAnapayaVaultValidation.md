# ConfigSCIONASCAServiceAnapayaVaultValidation

The validation option configures how the Anapaya Vault backend validate CSRs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | The subject option configures how the Anapaya Vault backend validates the subject of the CSRs. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionasca_service_anapaya_vault_validation import ConfigSCIONASCAServiceAnapayaVaultValidation

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCAServiceAnapayaVaultValidation from a JSON string
config_scionasca_service_anapaya_vault_validation_instance = ConfigSCIONASCAServiceAnapayaVaultValidation.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCAServiceAnapayaVaultValidation.to_json()

# convert the object into a dict
config_scionasca_service_anapaya_vault_validation_dict = config_scionasca_service_anapaya_vault_validation_instance.to_dict()
# create an instance of ConfigSCIONASCAServiceAnapayaVaultValidation from a dict
config_scionasca_service_anapaya_vault_validation_form_dict = config_scionasca_service_anapaya_vault_validation.from_dict(config_scionasca_service_anapaya_vault_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


