# CppkiCertificatesGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_chains** | [**List[ChainBrief]**](ChainBrief.md) | List of certificate chains | 

## Example

```python
from openapi_client.models.cppki_certificates_get_response_json import CppkiCertificatesGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCertificatesGetResponseJson from a JSON string
cppki_certificates_get_response_json_instance = CppkiCertificatesGetResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiCertificatesGetResponseJson.to_json()

# convert the object into a dict
cppki_certificates_get_response_json_dict = cppki_certificates_get_response_json_instance.to_dict()
# create an instance of CppkiCertificatesGetResponseJson from a dict
cppki_certificates_get_response_json_form_dict = cppki_certificates_get_response_json.from_dict(cppki_certificates_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


