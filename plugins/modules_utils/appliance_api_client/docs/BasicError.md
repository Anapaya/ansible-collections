# BasicError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | A human readable explanation specific to this occurrence of the problem that is helpful to locate the problem and give advice on how to proceed. Written in English and readable for engineers, usually not suited for non technical stakeholders and not localized. | [optional] 

## Example

```python
from openapi_client.models.basic_error import BasicError

# TODO update the JSON string below
json = "{}"
# create an instance of BasicError from a JSON string
basic_error_instance = BasicError.from_json(json)
# print the JSON string representation of the object
print BasicError.to_json()

# convert the object into a dict
basic_error_dict = basic_error_instance.to_dict()
# create an instance of BasicError from a dict
basic_error_form_dict = basic_error.from_dict(basic_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


