# CertificateChainForASAvailable

Check data for an explanation of this health check. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CertificateChainForASAvailableData**](CertificateChainForASAvailableData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.certificate_chain_for_as_available import CertificateChainForASAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateChainForASAvailable from a JSON string
certificate_chain_for_as_available_instance = CertificateChainForASAvailable.from_json(json)
# print the JSON string representation of the object
print CertificateChainForASAvailable.to_json()

# convert the object into a dict
certificate_chain_for_as_available_dict = certificate_chain_for_as_available_instance.to_dict()
# create an instance of CertificateChainForASAvailable from a dict
certificate_chain_for_as_available_form_dict = certificate_chain_for_as_available.from_dict(certificate_chain_for_as_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


