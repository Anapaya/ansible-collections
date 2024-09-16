# ConfigManagementApiBasicAuth

Basic auth configuration that restricts the access to the Anapaya appliance management API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable basic authentication for the Anapaya appliance management API. | [optional] 
**users** | [**List[ConfigManagementApiBasicAuthUser]**](ConfigManagementApiBasicAuthUser.md) | List of basic auth user credentials that are authorized to access the management API. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_api_basic_auth import ConfigManagementApiBasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiBasicAuth from a JSON string
config_management_api_basic_auth_instance = ConfigManagementApiBasicAuth.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiBasicAuth.to_json()

# convert the object into a dict
config_management_api_basic_auth_dict = config_management_api_basic_auth_instance.to_dict()
# create an instance of ConfigManagementApiBasicAuth from a dict
config_management_api_basic_auth_form_dict = config_management_api_basic_auth.from_dict(config_management_api_basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


