# CppkiCsrsGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_signing_requests** | [**List[CsrInfo]**](CsrInfo.md) | List of certificate signing requests | 

## Example

```python
from openapi_client.models.cppki_csrs_get_response_json import CppkiCsrsGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCsrsGetResponseJson from a JSON string
cppki_csrs_get_response_json_instance = CppkiCsrsGetResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiCsrsGetResponseJson.to_json()

# convert the object into a dict
cppki_csrs_get_response_json_dict = cppki_csrs_get_response_json_instance.to_dict()
# create an instance of CppkiCsrsGetResponseJson from a dict
cppki_csrs_get_response_json_form_dict = cppki_csrs_get_response_json.from_dict(cppki_csrs_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


