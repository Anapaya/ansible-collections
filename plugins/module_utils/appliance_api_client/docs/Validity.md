# Validity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_before** | **datetime** |  | 
**not_after** | **datetime** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.validity import Validity

# TODO update the JSON string below
json = "{}"
# create an instance of Validity from a JSON string
validity_instance = Validity.from_json(json)
# print the JSON string representation of the object
print Validity.to_json()

# convert the object into a dict
validity_dict = validity_instance.to_dict()
# create an instance of Validity from a dict
validity_form_dict = validity.from_dict(validity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


