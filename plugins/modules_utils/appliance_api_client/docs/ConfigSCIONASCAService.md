# ConfigSCIONASCAService

SCION CPPKI (Control Plane Public Key Infrastructure) CA service configuration data. This section defines how the anapaya-scion interacts with the SCION CPPKI CA service backend. It is only required for SCION ASes that act as a CA in their respective ISD.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anapaya_vault** | [**ConfigSCIONASCAServiceAnapayaVault**](ConfigSCIONASCAServiceAnapayaVault.md) |  | [optional] 
**external** | [**ConfigSCIONASCAServiceExternal**](ConfigSCIONASCAServiceExternal.md) |  | [optional] 
**service_type** | **str** | The type of CA service that is used by the appliance. | [optional] 

## Example

```python
from openapi_client.models.config_scionasca_service import ConfigSCIONASCAService

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASCAService from a JSON string
config_scionasca_service_instance = ConfigSCIONASCAService.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASCAService.to_json()

# convert the object into a dict
config_scionasca_service_dict = config_scionasca_service_instance.to_dict()
# create an instance of ConfigSCIONASCAService from a dict
config_scionasca_service_form_dict = config_scionasca_service.from_dict(config_scionasca_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


