# SoftwareInstallGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_info** | [**SoftwarePackageInstallInfo**](SoftwarePackageInstallInfo.md) |  | 

## Example

```python
from openapi_client.models.software_install_get_response_json import SoftwareInstallGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareInstallGetResponseJson from a JSON string
software_install_get_response_json_instance = SoftwareInstallGetResponseJson.from_json(json)
# print the JSON string representation of the object
print SoftwareInstallGetResponseJson.to_json()

# convert the object into a dict
software_install_get_response_json_dict = software_install_get_response_json_instance.to_dict()
# create an instance of SoftwareInstallGetResponseJson from a dict
software_install_get_response_json_form_dict = software_install_get_response_json.from_dict(software_install_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


