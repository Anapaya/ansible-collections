# ConfigPostResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | 
**metadata** | [**ConfigMetadata**](ConfigMetadata.md) |  | 

## Example

```python
from openapi_client.models.config_post_response_json import ConfigPostResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigPostResponseJson from a JSON string
config_post_response_json_instance = ConfigPostResponseJson.from_json(json)
# print the JSON string representation of the object
print ConfigPostResponseJson.to_json()

# convert the object into a dict
config_post_response_json_dict = config_post_response_json_instance.to_dict()
# create an instance of ConfigPostResponseJson from a dict
config_post_response_json_form_dict = config_post_response_json.from_dict(config_post_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


