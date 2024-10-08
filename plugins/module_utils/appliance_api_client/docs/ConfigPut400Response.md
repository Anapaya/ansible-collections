# ConfigPut400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A URI reference that uniquely identifies the problem type only in the context of the provided API. Opposed to the specification in RFC-7807, it is neither recommended to be dereferencable and point to a human-readable documentation nor globally unique for the problem type. | 
**title** | **str** | A short summary of the problem type. Written in English and readable for engineers, usually not suited for non technical stakeholders and not localized. | 
**status** | **int** | The HTTP status code generated by the origin server for this occurrence of the problem. | 
**detail** | **str** | A human readable explanation specific to this occurrence of the problem that is helpful to locate the problem and give advice on how to proceed. Written in English and readable for engineers, usually not suited for non technical stakeholders and not localized. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_put400_response import ConfigPut400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPut400Response from a JSON string
config_put400_response_instance = ConfigPut400Response.from_json(json)
# print the JSON string representation of the object
print ConfigPut400Response.to_json()

# convert the object into a dict
config_put400_response_dict = config_put400_response_instance.to_dict()
# create an instance of ConfigPut400Response from a dict
config_put400_response_form_dict = config_put400_response.from_dict(config_put400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


