# CppkiCsrsPostResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_signing_request** | [**CsrInfo**](CsrInfo.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.cppki_csrs_post_response_json import CppkiCsrsPostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiCsrsPostResponseJson from a JSON string
cppki_csrs_post_response_json_instance = CppkiCsrsPostResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiCsrsPostResponseJson.to_json()

# convert the object into a dict
cppki_csrs_post_response_json_dict = cppki_csrs_post_response_json_instance.to_dict()
# create an instance of CppkiCsrsPostResponseJson from a dict
cppki_csrs_post_response_json_form_dict = cppki_csrs_post_response_json.from_dict(cppki_csrs_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


