# CppkiCertificatesRenewPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**CertificateSubject**](CertificateSubject.md) |  | [optional] 
**issuers** | **List[str]** |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.cppki_certificates_renew_post_request import CppkiCertificatesRenewPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCertificatesRenewPostRequest from a JSON string
cppki_certificates_renew_post_request_instance = CppkiCertificatesRenewPostRequest.from_json(json)
# print the JSON string representation of the object
print CppkiCertificatesRenewPostRequest.to_json()

# convert the object into a dict
cppki_certificates_renew_post_request_dict = cppki_certificates_renew_post_request_instance.to_dict()
# create an instance of CppkiCertificatesRenewPostRequest from a dict
cppki_certificates_renew_post_request_form_dict = cppki_certificates_renew_post_request.from_dict(cppki_certificates_renew_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


