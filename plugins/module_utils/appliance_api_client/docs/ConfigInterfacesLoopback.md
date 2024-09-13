# ConfigInterfacesLoopback

List of loopback interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The list of addresses configured on the loopback interface. | [optional] 
**name** | **str** | The name of the loopback interface, which must have a &#39;loop&#39; prefix. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_loopback import ConfigInterfacesLoopback

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesLoopback from a JSON string
config_interfaces_loopback_instance = ConfigInterfacesLoopback.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesLoopback.to_json()

# convert the object into a dict
config_interfaces_loopback_dict = config_interfaces_loopback_instance.to_dict()
# create an instance of ConfigInterfacesLoopback from a dict
config_interfaces_loopback_form_dict = config_interfaces_loopback.from_dict(config_interfaces_loopback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


