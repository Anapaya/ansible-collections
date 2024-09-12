# LicensesGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenses** | [**List[LicensePayloadJson]**](LicensePayloadJson.md) | List of licenses. | 

## Example

```python
from openapi_client.models.licenses_get_response_json import LicensesGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesGetResponseJson from a JSON string
licenses_get_response_json_instance = LicensesGetResponseJson.from_json(json)
# print the JSON string representation of the object
print LicensesGetResponseJson.to_json()

# convert the object into a dict
licenses_get_response_json_dict = licenses_get_response_json_instance.to_dict()
# create an instance of LicensesGetResponseJson from a dict
licenses_get_response_json_form_dict = licenses_get_response_json.from_dict(licenses_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


