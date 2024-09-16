# SoftwarePackageGetResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**PackageInfo**](PackageInfo.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.software_package_get_response_json import SoftwarePackageGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackageGetResponseJson from a JSON string
software_package_get_response_json_instance = SoftwarePackageGetResponseJson.from_json(json)
# print the JSON string representation of the object
print SoftwarePackageGetResponseJson.to_json()

# convert the object into a dict
software_package_get_response_json_dict = software_package_get_response_json_instance.to_dict()
# create an instance of SoftwarePackageGetResponseJson from a dict
software_package_get_response_json_form_dict = software_package_get_response_json.from_dict(software_package_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


