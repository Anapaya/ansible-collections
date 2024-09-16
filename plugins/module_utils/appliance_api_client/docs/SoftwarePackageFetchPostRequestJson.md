# SoftwarePackageFetchPostRequestJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.software_package_fetch_post_request_json import SoftwarePackageFetchPostRequestJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackageFetchPostRequestJson from a JSON string
software_package_fetch_post_request_json_instance = SoftwarePackageFetchPostRequestJson.from_json(json)
# print the JSON string representation of the object
print SoftwarePackageFetchPostRequestJson.to_json()

# convert the object into a dict
software_package_fetch_post_request_json_dict = software_package_fetch_post_request_json_instance.to_dict()
# create an instance of SoftwarePackageFetchPostRequestJson from a dict
software_package_fetch_post_request_json_form_dict = software_package_fetch_post_request_json.from_dict(software_package_fetch_post_request_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


