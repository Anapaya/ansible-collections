# ConfigPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_put_request import ConfigPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPutRequest from a JSON string
config_put_request_instance = ConfigPutRequest.from_json(json)
# print the JSON string representation of the object
print ConfigPutRequest.to_json()

# convert the object into a dict
config_put_request_dict = config_put_request_instance.to_dict()
# create an instance of ConfigPutRequest from a dict
config_put_request_form_dict = config_put_request.from_dict(config_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


