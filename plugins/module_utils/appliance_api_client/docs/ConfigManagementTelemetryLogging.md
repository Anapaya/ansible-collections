# ConfigManagementTelemetryLogging

Configuration for shipping logs to a remote log aggregation system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logging_type** | **str** | The type of log aggregation system which is used. | [optional] 
**loki** | [**ConfigManagementTelemetryLoggingLoki**](ConfigManagementTelemetryLoggingLoki.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_telemetry_logging import ConfigManagementTelemetryLogging

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetryLogging from a JSON string
config_management_telemetry_logging_instance = ConfigManagementTelemetryLogging.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetryLogging.to_json()

# convert the object into a dict
config_management_telemetry_logging_dict = config_management_telemetry_logging_instance.to_dict()
# create an instance of ConfigManagementTelemetryLogging from a dict
config_management_telemetry_logging_form_dict = config_management_telemetry_logging.from_dict(config_management_telemetry_logging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


