# DebugServicesResponseJson

The list of services and service groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | **List[str]** | The list of services. | 
**groups** | [**List[DebugServicesGroup]**](DebugServicesGroup.md) | The list of service groups. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.debug_services_response_json import DebugServicesResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of DebugServicesResponseJson from a JSON string
debug_services_response_json_instance = DebugServicesResponseJson.from_json(json)
# print the JSON string representation of the object
print DebugServicesResponseJson.to_json()

# convert the object into a dict
debug_services_response_json_dict = debug_services_response_json_instance.to_dict()
# create an instance of DebugServicesResponseJson from a dict
debug_services_response_json_form_dict = debug_services_response_json.from_dict(debug_services_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


