# SiblingInterfaceUp

Check data for an explanation of this health check. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SiblingInterfaceUpData**](SiblingInterfaceUpData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.sibling_interface_up import SiblingInterfaceUp

# TODO update the JSON string below
json = "{}"
# create an instance of SiblingInterfaceUp from a JSON string
sibling_interface_up_instance = SiblingInterfaceUp.from_json(json)
# print the JSON string representation of the object
print SiblingInterfaceUp.to_json()

# convert the object into a dict
sibling_interface_up_dict = sibling_interface_up_instance.to_dict()
# create an instance of SiblingInterfaceUp from a dict
sibling_interface_up_form_dict = sibling_interface_up.from_dict(sibling_interface_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


