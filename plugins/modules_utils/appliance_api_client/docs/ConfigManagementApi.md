# ConfigManagementApi

Anapaya appliance management API configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**ConfigManagementApiBasicAuth**](ConfigManagementApiBasicAuth.md) |  | [optional] 
**listeners** | [**List[ConfigManagementApiListener]**](ConfigManagementApiListener.md) | List of management API listeners that define where the API is exposed | [optional] 
**oauth** | [**ConfigManagementApiOauth**](ConfigManagementApiOauth.md) |  | [optional] 
**unprotected** | **bool** | Whether the management API is allowed to be exposed without authentication. Always make sure to properly protect your API. | [optional] [default to False]

## Example

```python
from openapi_client.models.config_management_api import ConfigManagementApi

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApi from a JSON string
config_management_api_instance = ConfigManagementApi.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApi.to_json()

# convert the object into a dict
config_management_api_dict = config_management_api_instance.to_dict()
# create an instance of ConfigManagementApi from a dict
config_management_api_form_dict = config_management_api.from_dict(config_management_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


