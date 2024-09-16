# ApplianceDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | The hostname of the appliance. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.appliance_description import ApplianceDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ApplianceDescription from a JSON string
appliance_description_instance = ApplianceDescription.from_json(json)
# print the JSON string representation of the object
print ApplianceDescription.to_json()

# convert the object into a dict
appliance_description_dict = appliance_description_instance.to_dict()
# create an instance of ApplianceDescription from a dict
appliance_description_form_dict = appliance_description.from_dict(appliance_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


