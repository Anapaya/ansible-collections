# DebugServicesGroup

The service group and its services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The group name. | 
**services** | **List[str]** | Services in the group. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.debug_services_group import DebugServicesGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DebugServicesGroup from a JSON string
debug_services_group_instance = DebugServicesGroup.from_json(json)
# print the JSON string representation of the object
print DebugServicesGroup.to_json()

# convert the object into a dict
debug_services_group_dict = debug_services_group_instance.to_dict()
# create an instance of DebugServicesGroup from a dict
debug_services_group_form_dict = debug_services_group.from_dict(debug_services_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


