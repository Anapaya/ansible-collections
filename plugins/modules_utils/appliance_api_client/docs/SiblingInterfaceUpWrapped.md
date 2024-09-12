# SiblingInterfaceUpWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from openapi_client.models.sibling_interface_up_wrapped import SiblingInterfaceUpWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of SiblingInterfaceUpWrapped from a JSON string
sibling_interface_up_wrapped_instance = SiblingInterfaceUpWrapped.from_json(json)
# print the JSON string representation of the object
print SiblingInterfaceUpWrapped.to_json()

# convert the object into a dict
sibling_interface_up_wrapped_dict = sibling_interface_up_wrapped_instance.to_dict()
# create an instance of SiblingInterfaceUpWrapped from a dict
sibling_interface_up_wrapped_form_dict = sibling_interface_up_wrapped.from_dict(sibling_interface_up_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


