# LicensePayloadJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_id** | **str** | The license ID. | 
**appliance_id** | **str** | The appliance ID for which the license is valid. | 
**type** | [**LicenseType**](LicenseType.md) |  | 
**issued** | **datetime** | The date and time when the license was issued. | 
**validity** | [**LicenseValidity**](LicenseValidity.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.license_payload_json import LicensePayloadJson

# TODO update the JSON string below
json = "{}"
# create an instance of LicensePayloadJson from a JSON string
license_payload_json_instance = LicensePayloadJson.from_json(json)
# print the JSON string representation of the object
print LicensePayloadJson.to_json()

# convert the object into a dict
license_payload_json_dict = license_payload_json_instance.to_dict()
# create an instance of LicensePayloadJson from a dict
license_payload_json_form_dict = license_payload_json.from_dict(license_payload_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


