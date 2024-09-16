# LicenseRequestGetResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the license request object. | 
**data** | [**LicenseRequestData**](LicenseRequestData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.license_request_get_response_json import LicenseRequestGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRequestGetResponseJson from a JSON string
license_request_get_response_json_instance = LicenseRequestGetResponseJson.from_json(json)
# print the JSON string representation of the object
print LicenseRequestGetResponseJson.to_json()

# convert the object into a dict
license_request_get_response_json_dict = license_request_get_response_json_instance.to_dict()
# create an instance of LicenseRequestGetResponseJson from a dict
license_request_get_response_json_form_dict = license_request_get_response_json.from_dict(license_request_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


