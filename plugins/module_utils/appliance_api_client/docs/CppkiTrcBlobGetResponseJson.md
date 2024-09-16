# CppkiTrcBlobGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trc** | **str** | PEM encoded TRC | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.cppki_trc_blob_get_response_json import CppkiTrcBlobGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiTrcBlobGetResponseJson from a JSON string
cppki_trc_blob_get_response_json_instance = CppkiTrcBlobGetResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiTrcBlobGetResponseJson.to_json()

# convert the object into a dict
cppki_trc_blob_get_response_json_dict = cppki_trc_blob_get_response_json_instance.to_dict()
# create an instance of CppkiTrcBlobGetResponseJson from a dict
cppki_trc_blob_get_response_json_form_dict = cppki_trc_blob_get_response_json.from_dict(cppki_trc_blob_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


