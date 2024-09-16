# CertificateSigningRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**CertificateSubject**](CertificateSubject.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.certificate_signing_request import CertificateSigningRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateSigningRequest from a JSON string
certificate_signing_request_instance = CertificateSigningRequest.from_json(json)
# print the JSON string representation of the object
print CertificateSigningRequest.to_json()

# convert the object into a dict
certificate_signing_request_dict = certificate_signing_request_instance.to_dict()
# create an instance of CertificateSigningRequest from a dict
certificate_signing_request_form_dict = certificate_signing_request.from_dict(certificate_signing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


