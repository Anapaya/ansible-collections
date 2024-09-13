# SchemasValidity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_before** | **datetime** | The time at which the validity period starts. | 
**not_after** | **datetime** | The time at which the validity period stops. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.schemas_validity import SchemasValidity

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasValidity from a JSON string
schemas_validity_instance = SchemasValidity.from_json(json)
# print the JSON string representation of the object
print SchemasValidity.to_json()

# convert the object into a dict
schemas_validity_dict = schemas_validity_instance.to_dict()
# create an instance of SchemasValidity from a dict
schemas_validity_form_dict = schemas_validity.from_dict(schemas_validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


