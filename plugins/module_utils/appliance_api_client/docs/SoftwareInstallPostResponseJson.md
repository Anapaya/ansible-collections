# SoftwareInstallPostResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_info** | [**SoftwarePackageInstallInfo**](SoftwarePackageInstallInfo.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.software_install_post_response_json import SoftwareInstallPostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareInstallPostResponseJson from a JSON string
software_install_post_response_json_instance = SoftwareInstallPostResponseJson.from_json(json)
# print the JSON string representation of the object
print SoftwareInstallPostResponseJson.to_json()

# convert the object into a dict
software_install_post_response_json_dict = software_install_post_response_json_instance.to_dict()
# create an instance of SoftwareInstallPostResponseJson from a dict
software_install_post_response_json_form_dict = software_install_post_response_json.from_dict(software_install_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


