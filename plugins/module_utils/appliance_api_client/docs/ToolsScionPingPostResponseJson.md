# ToolsScionPingPostResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**PingSummary**](PingSummary.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.tools_scion_ping_post_response_json import ToolsScionPingPostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsScionPingPostResponseJson from a JSON string
tools_scion_ping_post_response_json_instance = ToolsScionPingPostResponseJson.from_json(json)
# print the JSON string representation of the object
print ToolsScionPingPostResponseJson.to_json()

# convert the object into a dict
tools_scion_ping_post_response_json_dict = tools_scion_ping_post_response_json_instance.to_dict()
# create an instance of ToolsScionPingPostResponseJson from a dict
tools_scion_ping_post_response_json_form_dict = tools_scion_ping_post_response_json.from_dict(tools_scion_ping_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


