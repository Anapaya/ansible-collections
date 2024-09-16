# ConfigManagementTelemetryLoggingLoki

Loki configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basic_auth** | [**ConfigManagementTelemetryLoggingLokiBasicAuth**](ConfigManagementTelemetryLoggingLokiBasicAuth.md) |  | [optional] 
**tls_config** | [**ConfigManagementTelemetryLoggingLokiTlsConfig**](ConfigManagementTelemetryLoggingLokiTlsConfig.md) |  | [optional] 
**url** | **str** | The url which is used to push logs to Loki. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_telemetry_logging_loki import ConfigManagementTelemetryLoggingLoki

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetryLoggingLoki from a JSON string
config_management_telemetry_logging_loki_instance = ConfigManagementTelemetryLoggingLoki.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetryLoggingLoki.to_json()

# convert the object into a dict
config_management_telemetry_logging_loki_dict = config_management_telemetry_logging_loki_instance.to_dict()
# create an instance of ConfigManagementTelemetryLoggingLoki from a dict
config_management_telemetry_logging_loki_form_dict = config_management_telemetry_logging_loki.from_dict(config_management_telemetry_logging_loki_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


