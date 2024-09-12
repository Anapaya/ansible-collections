# ConfigAdvancedServiceCustomizations

List of service customizations that should be configured on the Anapaya appliance system, uniquely identified by the service type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether the service customization should be disabled. | [optional] [default to False]
**service_type** | **str** | The service type for which the customized template is provided. | 
**template** | **str** | The actual customized template for the service. | 

## Example

```python
from openapi_client.models.config_advanced_service_customizations import ConfigAdvancedServiceCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAdvancedServiceCustomizations from a JSON string
config_advanced_service_customizations_instance = ConfigAdvancedServiceCustomizations.from_json(json)
# print the JSON string representation of the object
print ConfigAdvancedServiceCustomizations.to_json()

# convert the object into a dict
config_advanced_service_customizations_dict = config_advanced_service_customizations_instance.to_dict()
# create an instance of ConfigAdvancedServiceCustomizations from a dict
config_advanced_service_customizations_form_dict = config_advanced_service_customizations.from_dict(config_advanced_service_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


