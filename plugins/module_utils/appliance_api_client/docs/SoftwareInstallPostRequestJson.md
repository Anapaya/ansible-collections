# SoftwareInstallPostRequestJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**force** | **bool** |  | [optional] [default to False]
**skip_signature_verification** | **bool** |  | [optional] [default to False]

## Example

```python
from ansible.module_utils.appliance_api_client.models.software_install_post_request_json import SoftwareInstallPostRequestJson

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareInstallPostRequestJson from a JSON string
software_install_post_request_json_instance = SoftwareInstallPostRequestJson.from_json(json)
# print the JSON string representation of the object
print SoftwareInstallPostRequestJson.to_json()

# convert the object into a dict
software_install_post_request_json_dict = software_install_post_request_json_instance.to_dict()
# create an instance of SoftwareInstallPostRequestJson from a dict
software_install_post_request_json_form_dict = software_install_post_request_json.from_dict(software_install_post_request_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


