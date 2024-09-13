# ConfigSCIONASCAServiceExternal

The configuration data for the External SCION CPPKI CA service. This section is provided only when the CA service is of type External, i.e., is not operated by Anapaya.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address where the external SCION CPPKI CA service can be reached. | [optional] 
**client_id** | **str** | The client ID that is used to authenticate with the CA service. The client ID is set in the &#39;sub&#39; and &#39;iss&#39; claim of the generated JWT. If unset, a generic client ID based on the ISD-AS is used. | [optional] 
**shared_secret** | **str** | The shared secrets between the appliance and the CA service (used to generate JWTs for authentication). | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionasca_service_external import ConfigSCIONASCAServiceExternal

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCAServiceExternal from a JSON string
config_scionasca_service_external_instance = ConfigSCIONASCAServiceExternal.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCAServiceExternal.to_json()

# convert the object into a dict
config_scionasca_service_external_dict = config_scionasca_service_external_instance.to_dict()
# create an instance of ConfigSCIONASCAServiceExternal from a dict
config_scionasca_service_external_form_dict = config_scionasca_service_external.from_dict(config_scionasca_service_external_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


