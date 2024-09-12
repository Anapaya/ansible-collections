# ConfigPutResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | 
**metadata** | [**ConfigMetadata**](ConfigMetadata.md) |  | 

## Example

```python
from openapi_client.models.config_put_response_json import ConfigPutResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPutResponseJson from a JSON string
config_put_response_json_instance = ConfigPutResponseJson.from_json(json)
# print the JSON string representation of the object
print ConfigPutResponseJson.to_json()

# convert the object into a dict
config_put_response_json_dict = config_put_response_json_instance.to_dict()
# create an instance of ConfigPutResponseJson from a dict
config_put_response_json_form_dict = config_put_response_json.from_dict(config_put_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


