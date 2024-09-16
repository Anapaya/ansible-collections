# ConfigAdvanced

The necessary configuration data for the advanced section of the Anapaya appliance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_customizations** | [**List[ConfigAdvancedServiceCustomization]**](ConfigAdvancedServiceCustomization.md) | The list of service-customizations on the Anapaya appliance. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_advanced import ConfigAdvanced

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAdvanced from a JSON string
config_advanced_instance = ConfigAdvanced.from_json(json)
# print the JSON string representation of the object
print ConfigAdvanced.to_json()

# convert the object into a dict
config_advanced_dict = config_advanced_instance.to_dict()
# create an instance of ConfigAdvanced from a dict
config_advanced_form_dict = config_advanced.from_dict(config_advanced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


