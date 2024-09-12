# CppkiCertificatesPostResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_chain** | [**ChainBrief**](ChainBrief.md) |  | 

## Example

```python
from openapi_client.models.cppki_certificates_post_response_json import CppkiCertificatesPostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCertificatesPostResponseJson from a JSON string
cppki_certificates_post_response_json_instance = CppkiCertificatesPostResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiCertificatesPostResponseJson.to_json()

# convert the object into a dict
cppki_certificates_post_response_json_dict = cppki_certificates_post_response_json_instance.to_dict()
# create an instance of CppkiCertificatesPostResponseJson from a dict
cppki_certificates_post_response_json_form_dict = cppki_certificates_post_response_json.from_dict(cppki_certificates_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


