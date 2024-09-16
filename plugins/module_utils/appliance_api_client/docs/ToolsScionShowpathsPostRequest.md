# ToolsScionShowpathsPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run** | [**ShowpathsRun**](ShowpathsRun.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.tools_scion_showpaths_post_request import ToolsScionShowpathsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsScionShowpathsPostRequest from a JSON string
tools_scion_showpaths_post_request_instance = ToolsScionShowpathsPostRequest.from_json(json)
# print the JSON string representation of the object
print ToolsScionShowpathsPostRequest.to_json()

# convert the object into a dict
tools_scion_showpaths_post_request_dict = tools_scion_showpaths_post_request_instance.to_dict()
# create an instance of ToolsScionShowpathsPostRequest from a dict
tools_scion_showpaths_post_request_form_dict = tools_scion_showpaths_post_request.from_dict(tools_scion_showpaths_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


