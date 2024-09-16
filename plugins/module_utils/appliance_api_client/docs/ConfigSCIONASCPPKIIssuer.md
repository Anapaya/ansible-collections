# ConfigSCIONASCPPKIIssuer

The configuration for an issuing AS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd_as** | **str** | The ISD-AS identifier of the issuing AS. | 
**priority** | **int** | The priority of the issuing AS. The appliance attempts to get certificates issued from the AS with the highest priority. The value 0 indicates the highest priority, higher numbers are lower priority. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionascppki_issuer import ConfigSCIONASCPPKIIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCPPKIIssuer from a JSON string
config_scionascppki_issuer_instance = ConfigSCIONASCPPKIIssuer.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCPPKIIssuer.to_json()

# convert the object into a dict
config_scionascppki_issuer_dict = config_scionascppki_issuer_instance.to_dict()
# create an instance of ConfigSCIONASCPPKIIssuer from a dict
config_scionascppki_issuer_form_dict = config_scionascppki_issuer.from_dict(config_scionascppki_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


