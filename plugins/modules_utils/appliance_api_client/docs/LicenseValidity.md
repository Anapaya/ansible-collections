# LicenseValidity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_date** | **datetime** | The date and time when the license becomes valid. | 
**final_date** | **datetime** | The date and time when the license expires. | 

## Example

```python
from openapi_client.models.license_validity import LicenseValidity

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseValidity from a JSON string
license_validity_instance = LicenseValidity.from_json(json)
# print the JSON string representation of the object
print LicenseValidity.to_json()

# convert the object into a dict
license_validity_dict = license_validity_instance.to_dict()
# create an instance of LicenseValidity from a dict
license_validity_form_dict = license_validity.from_dict(license_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


