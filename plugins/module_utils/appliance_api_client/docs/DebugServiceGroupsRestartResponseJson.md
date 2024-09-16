# DebugServiceGroupsRestartResponseJson

The list restarted services of the group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | **List[str]** | Successfully restarted services. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.debug_service_groups_restart_response_json import DebugServiceGroupsRestartResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of DebugServiceGroupsRestartResponseJson from a JSON string
debug_service_groups_restart_response_json_instance = DebugServiceGroupsRestartResponseJson.from_json(json)
# print the JSON string representation of the object
print DebugServiceGroupsRestartResponseJson.to_json()

# convert the object into a dict
debug_service_groups_restart_response_json_dict = debug_service_groups_restart_response_json_instance.to_dict()
# create an instance of DebugServiceGroupsRestartResponseJson from a dict
debug_service_groups_restart_response_json_form_dict = debug_service_groups_restart_response_json.from_dict(debug_service_groups_restart_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


