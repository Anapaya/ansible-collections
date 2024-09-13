# CppkiCertificatesRequestPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | PEM encoded CSR | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.cppki_certificates_request_post_request import CppkiCertificatesRequestPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCertificatesRequestPostRequest from a JSON string
cppki_certificates_request_post_request_instance = CppkiCertificatesRequestPostRequest.from_json(json)
# print the JSON string representation of the object
print CppkiCertificatesRequestPostRequest.to_json()

# convert the object into a dict
cppki_certificates_request_post_request_dict = cppki_certificates_request_post_request_instance.to_dict()
# create an instance of CppkiCertificatesRequestPostRequest from a dict
cppki_certificates_request_post_request_form_dict = cppki_certificates_request_post_request.from_dict(cppki_certificates_request_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


