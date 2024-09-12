# ConfigAdvancedServiceCustomization

List of service customizations that should be configured on the Anapaya appliance system, uniquely identified by the service type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether the service customization should be disabled. | [optional] [default to False]
**service_type** | **str** | The service type for which the customized template is provided. | 
**template** | **str** | The actual customized template for the service. | 

## Example

```python
from openapi_client.models.config_advanced_service_customization import ConfigAdvancedServiceCustomization

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAdvancedServiceCustomization from a JSON string
config_advanced_service_customization_instance = ConfigAdvancedServiceCustomization.from_json(json)
# print the JSON string representation of the object
print ConfigAdvancedServiceCustomization.to_json()

# convert the object into a dict
config_advanced_service_customization_dict = config_advanced_service_customization_instance.to_dict()
# create an instance of ConfigAdvancedServiceCustomization from a dict
config_advanced_service_customization_form_dict = config_advanced_service_customization.from_dict(config_advanced_service_customization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


