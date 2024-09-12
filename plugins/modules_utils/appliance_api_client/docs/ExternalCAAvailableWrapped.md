# ExternalCAAvailableWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from openapi_client.models.external_ca_available_wrapped import ExternalCAAvailableWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCAAvailableWrapped from a JSON string
external_ca_available_wrapped_instance = ExternalCAAvailableWrapped.from_json(json)
# print the JSON string representation of the object
print ExternalCAAvailableWrapped.to_json()

# convert the object into a dict
external_ca_available_wrapped_dict = external_ca_available_wrapped_instance.to_dict()
# create an instance of ExternalCAAvailableWrapped from a dict
external_ca_available_wrapped_form_dict = external_ca_available_wrapped.from_dict(external_ca_available_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


