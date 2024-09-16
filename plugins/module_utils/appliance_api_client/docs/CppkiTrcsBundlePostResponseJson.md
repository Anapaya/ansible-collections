# CppkiTrcsBundlePostResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trcs** | [**List[TRC]**](TRC.md) | List of TRCs. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.cppki_trcs_bundle_post_response_json import CppkiTrcsBundlePostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of CppkiTrcsBundlePostResponseJson from a JSON string
cppki_trcs_bundle_post_response_json_instance = CppkiTrcsBundlePostResponseJson.from_json(json)
# print the JSON string representation of the object
print CppkiTrcsBundlePostResponseJson.to_json()

# convert the object into a dict
cppki_trcs_bundle_post_response_json_dict = cppki_trcs_bundle_post_response_json_instance.to_dict()
# create an instance of CppkiTrcsBundlePostResponseJson from a dict
cppki_trcs_bundle_post_response_json_form_dict = cppki_trcs_bundle_post_response_json.from_dict(cppki_trcs_bundle_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


