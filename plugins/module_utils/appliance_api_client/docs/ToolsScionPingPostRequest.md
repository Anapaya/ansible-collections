# ToolsScionPingPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run** | [**PingRun**](PingRun.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.tools_scion_ping_post_request import ToolsScionPingPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsScionPingPostRequest from a JSON string
tools_scion_ping_post_request_instance = ToolsScionPingPostRequest.from_json(json)
# print the JSON string representation of the object
print ToolsScionPingPostRequest.to_json()

# convert the object into a dict
tools_scion_ping_post_request_dict = tools_scion_ping_post_request_instance.to_dict()
# create an instance of ToolsScionPingPostRequest from a dict
tools_scion_ping_post_request_form_dict = tools_scion_ping_post_request.from_dict(tools_scion_ping_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


