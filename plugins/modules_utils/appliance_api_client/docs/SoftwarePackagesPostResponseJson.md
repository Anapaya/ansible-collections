# SoftwarePackagesPostResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**PackageInfo**](PackageInfo.md) |  | 

## Example

```python
from openapi_client.models.software_packages_post_response_json import SoftwarePackagesPostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackagesPostResponseJson from a JSON string
software_packages_post_response_json_instance = SoftwarePackagesPostResponseJson.from_json(json)
# print the JSON string representation of the object
print SoftwarePackagesPostResponseJson.to_json()

# convert the object into a dict
software_packages_post_response_json_dict = software_packages_post_response_json_instance.to_dict()
# create an instance of SoftwarePackagesPostResponseJson from a dict
software_packages_post_response_json_form_dict = software_packages_post_response_json.from_dict(software_packages_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


