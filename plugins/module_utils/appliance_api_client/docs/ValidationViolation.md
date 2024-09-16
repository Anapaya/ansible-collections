# ValidationViolation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to the config item where the violation happened. | 
**reason** | **str** | The reason for the violation. | 
**detail** | **str** | Additional details for this violation. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.validation_violation import ValidationViolation

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationViolation from a JSON string
validation_violation_instance = ValidationViolation.from_json(json)
# print the JSON string representation of the object
print ValidationViolation.to_json()

# convert the object into a dict
validation_violation_dict = validation_violation_instance.to_dict()
# create an instance of ValidationViolation from a dict
validation_violation_form_dict = validation_violation.from_dict(validation_violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


