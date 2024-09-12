# ConfigManagement

The necessary configuration data for the management of the  Anapaya appliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | [**ConfigManagementApi**](ConfigManagementApi.md) |  | [optional] 
**hostname** | **str** | The hostname of the Anapaya appliance host. It is used to identify the host in the telemetry data; thus, each host should have a unique hostname. | [optional] [default to 'anapaya-appliance']
**remote_repository** | [**ConfigManagementRemoteRepository**](ConfigManagementRemoteRepository.md) |  | [optional] 
**ssh** | [**ConfigManagementSsh**](ConfigManagementSsh.md) |  | [optional] 
**telemetry** | [**ConfigManagementTelemetry**](ConfigManagementTelemetry.md) |  | [optional] 

## Example

```python
from openapi_client.models.config_management import ConfigManagement

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagement from a JSON string
config_management_instance = ConfigManagement.from_json(json)
# print the JSON string representation of the object
print ConfigManagement.to_json()

# convert the object into a dict
config_management_dict = config_management_instance.to_dict()
# create an instance of ConfigManagement from a dict
config_management_form_dict = config_management.from_dict(config_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


