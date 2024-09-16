# LicenseType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **str** | The product for which the license is valid. | 
**tier** | **str** | The tier for which the license is valid. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.license_type import LicenseType

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseType from a JSON string
license_type_instance = LicenseType.from_json(json)
# print the JSON string representation of the object
print LicenseType.to_json()

# convert the object into a dict
license_type_dict = license_type_instance.to_dict()
# create an instance of LicenseType from a dict
license_type_form_dict = license_type.from_dict(license_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


