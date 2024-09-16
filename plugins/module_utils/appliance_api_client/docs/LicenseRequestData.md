# LicenseRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | The appliance ID for which the license is requested. | 
**scion_activation_date** | **datetime** | The date and time when SCION was first activated on the appliance. | [optional] 
**appliance_version** | **str** | The version of the appliance for which the license is requested. | 
**appliance_description** | [**ApplianceDescription**](ApplianceDescription.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.license_request_data import LicenseRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseRequestData from a JSON string
license_request_data_instance = LicenseRequestData.from_json(json)
# print the JSON string representation of the object
print LicenseRequestData.to_json()

# convert the object into a dict
license_request_data_dict = license_request_data_instance.to_dict()
# create an instance of LicenseRequestData from a dict
license_request_data_form_dict = license_request_data.from_dict(license_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


