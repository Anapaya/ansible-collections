# ExternalInterfaceUpWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.external_interface_up_wrapped import ExternalInterfaceUpWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalInterfaceUpWrapped from a JSON string
external_interface_up_wrapped_instance = ExternalInterfaceUpWrapped.from_json(json)
# print the JSON string representation of the object
print ExternalInterfaceUpWrapped.to_json()

# convert the object into a dict
external_interface_up_wrapped_dict = external_interface_up_wrapped_instance.to_dict()
# create an instance of ExternalInterfaceUpWrapped from a dict
external_interface_up_wrapped_form_dict = external_interface_up_wrapped.from_dict(external_interface_up_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


