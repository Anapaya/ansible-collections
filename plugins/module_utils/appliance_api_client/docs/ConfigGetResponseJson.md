# ConfigGetResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**Config**](Config.md) |  | 
**metadata** | [**ConfigMetadata**](ConfigMetadata.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_get_response_json import ConfigGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigGetResponseJson from a JSON string
config_get_response_json_instance = ConfigGetResponseJson.from_json(json)
# print the JSON string representation of the object
print ConfigGetResponseJson.to_json()

# convert the object into a dict
config_get_response_json_dict = config_get_response_json_instance.to_dict()
# create an instance of ConfigGetResponseJson from a dict
config_get_response_json_form_dict = config_get_response_json.from_dict(config_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


