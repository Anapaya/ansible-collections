# LicenseStatusGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the licensing. Indicates whether a valid license is present on the appliance, or whether the appliance is in grace period, or if the appliance functionality is restricted.  | 
**license_id** | **str** | The license ID of the license which is currently active on the appliance. Only set in valid-license status.  | [optional] 
**expiry** | **datetime** | The time up to which the current status remains unchanged without interaction. For grace and trial periods, it indicates the end of these periods, while for a license it indicates the expiration date.  | [optional] 
**enforcer_disabled** | **bool** | Whether the license enforcer is disabled via feature flag.  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.license_status_get_response_json import LicenseStatusGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseStatusGetResponseJson from a JSON string
license_status_get_response_json_instance = LicenseStatusGetResponseJson.from_json(json)
# print the JSON string representation of the object
print LicenseStatusGetResponseJson.to_json()

# convert the object into a dict
license_status_get_response_json_dict = license_status_get_response_json_instance.to_dict()
# create an instance of LicenseStatusGetResponseJson from a dict
license_status_get_response_json_form_dict = license_status_get_response_json.from_dict(license_status_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


