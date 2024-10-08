# CertificateChainForASAvailableData

The certificate chain for the AS is available. A certificate chain is required to sign the SCION control plane messages. If the certificate chain is not present, the local AS will not be able to fully join the SCION network. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd_as** | **str** |  | 
**subject_key_id** | **str** | The subject key identifier of the AS certificate. | 
**issuer** | **str** |  | 
**valid_until** | **datetime** | The time until the certificate is valid for. This is the minimum of the validity.not_before and the trc.validity.not_before time. A certificate chain is only cosidered valid for as long as the TRC that contains the corresponding root certificate is valid.  | 
**in_grace_period** | **bool** | Indicates if the certificate is only verifiable with a TRC that is currently in grace period. As soon as the grace period expires, the certificate will be considered invalid.  | 
**validity** | [**SchemasValidity**](SchemasValidity.md) |  | 
**trc** | [**TRCInfo**](TRCInfo.md) |  | 
**data_type** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.certificate_chain_for_as_available_data import CertificateChainForASAvailableData

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateChainForASAvailableData from a JSON string
certificate_chain_for_as_available_data_instance = CertificateChainForASAvailableData.from_json(json)
# print the JSON string representation of the object
print CertificateChainForASAvailableData.to_json()

# convert the object into a dict
certificate_chain_for_as_available_data_dict = certificate_chain_for_as_available_data_instance.to_dict()
# create an instance of CertificateChainForASAvailableData from a dict
certificate_chain_for_as_available_data_form_dict = certificate_chain_for_as_available_data.from_dict(certificate_chain_for_as_available_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


