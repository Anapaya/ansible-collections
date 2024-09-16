# ConfigSCIONASCPPKI

SCION CPPKI configuration for the SCION AS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_auto_renewal** | **bool** | Whether automatic renewal of AS certificates should be disabled. Usually, this value should not be set. By disabling certificate renewal, the appliance is set into a manual mode where new AS certificates must be provisioned manually and periodically. | [optional] 
**issuers** | [**List[ConfigSCIONASCPPKIIssuer]**](ConfigSCIONASCPPKIIssuer.md) | The SCION CPPKI Issuers that issue certificates for the local SCION AS. The list of issuers is tried in order of their priority. If no issuers are set explicitly, the renewal process will use the issuer of the newest existing SCION CPPKI AS Certificate. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionascppki import ConfigSCIONASCPPKI

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCPPKI from a JSON string
config_scionascppki_instance = ConfigSCIONASCPPKI.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCPPKI.to_json()

# convert the object into a dict
config_scionascppki_dict = config_scionascppki_instance.to_dict()
# create an instance of ConfigSCIONASCPPKI from a dict
config_scionascppki_form_dict = config_scionascppki.from_dict(config_scionascppki_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


