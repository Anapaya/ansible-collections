# SoftwareInstalledGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**checksum** | **str** | Checksum of the installed package. | 

## Example

```python
from openapi_client.models.software_installed_get_response_json import SoftwareInstalledGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareInstalledGetResponseJson from a JSON string
software_installed_get_response_json_instance = SoftwareInstalledGetResponseJson.from_json(json)
# print the JSON string representation of the object
print SoftwareInstalledGetResponseJson.to_json()

# convert the object into a dict
software_installed_get_response_json_dict = software_installed_get_response_json_instance.to_dict()
# create an instance of SoftwareInstalledGetResponseJson from a dict
software_installed_get_response_json_form_dict = software_installed_get_response_json.from_dict(software_installed_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


