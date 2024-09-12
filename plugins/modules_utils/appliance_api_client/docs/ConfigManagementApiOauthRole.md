# ConfigManagementApiOauthRole

List of roles which are used for OAuth.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** | List of aliases for the role. This is useful for mapping different role names from different identity providers to the same role in the appliance. If no alias are configured for a role the default aliases are &#39;appliance.&lt;role&gt;&#39;, &#39;appliance/&lt;role&gt;&#39;, and &#39;appliance:&lt;role&gt;&#39;. | [optional] 
**role** | **str** | Name of the role. | [optional] 

## Example

```python
from openapi_client.models.config_management_api_oauth_role import ConfigManagementApiOauthRole

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementApiOauthRole from a JSON string
config_management_api_oauth_role_instance = ConfigManagementApiOauthRole.from_json(json)
# print the JSON string representation of the object
print ConfigManagementApiOauthRole.to_json()

# convert the object into a dict
config_management_api_oauth_role_dict = config_management_api_oauth_role_instance.to_dict()
# create an instance of ConfigManagementApiOauthRole from a dict
config_management_api_oauth_role_form_dict = config_management_api_oauth_role.from_dict(config_management_api_oauth_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


