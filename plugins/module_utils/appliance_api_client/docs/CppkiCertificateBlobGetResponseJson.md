# CppkiCertificateBlobGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_chain** | **str** | PEM encoded certificate chain | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.cppki_certificate_blob_get_response_json import CppkiCertificateBlobGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCertificateBlobGetResponseJson from a JSON string
cppki_certificate_blob_get_response_json_instance = CppkiCertificateBlobGetResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiCertificateBlobGetResponseJson.to_json()

# convert the object into a dict
cppki_certificate_blob_get_response_json_dict = cppki_certificate_blob_get_response_json_instance.to_dict()
# create an instance of CppkiCertificateBlobGetResponseJson from a dict
cppki_certificate_blob_get_response_json_form_dict = cppki_certificate_blob_get_response_json.from_dict(cppki_certificate_blob_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


