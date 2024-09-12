# SoftwarePackageDeleteResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**PackageInfo**](PackageInfo.md) |  | 

## Example

```python
from openapi_client.models.software_package_delete_response_json import SoftwarePackageDeleteResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackageDeleteResponseJson from a JSON string
software_package_delete_response_json_instance = SoftwarePackageDeleteResponseJson.from_json(json)
# print the JSON string representation of the object
print SoftwarePackageDeleteResponseJson.to_json()

# convert the object into a dict
software_package_delete_response_json_dict = software_package_delete_response_json_instance.to_dict()
# create an instance of SoftwarePackageDeleteResponseJson from a dict
software_package_delete_response_json_form_dict = software_package_delete_response_json.from_dict(software_package_delete_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


