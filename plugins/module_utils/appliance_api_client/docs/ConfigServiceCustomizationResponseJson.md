# ConfigServiceCustomizationResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_customization** | [**ConfigAdvancedServiceCustomization**](ConfigAdvancedServiceCustomization.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_service_customization_response_json import ConfigServiceCustomizationResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigServiceCustomizationResponseJson from a JSON string
config_service_customization_response_json_instance = ConfigServiceCustomizationResponseJson.from_json(json)
# print the JSON string representation of the object
print ConfigServiceCustomizationResponseJson.to_json()

# convert the object into a dict
config_service_customization_response_json_dict = config_service_customization_response_json_instance.to_dict()
# create an instance of ConfigServiceCustomizationResponseJson from a dict
config_service_customization_response_json_form_dict = config_service_customization_response_json.from_dict(config_service_customization_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


