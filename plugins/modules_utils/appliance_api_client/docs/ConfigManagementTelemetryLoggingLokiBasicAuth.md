# ConfigManagementTelemetryLoggingLokiBasicAuth

Basic auth configuration for sending log lines to Loki.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password to use for basic auth. | [optional] 
**username** | **str** | The username to use for basic auth. | [optional] 

## Example

```python
from openapi_client.models.config_management_telemetry_logging_loki_basic_auth import ConfigManagementTelemetryLoggingLokiBasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetryLoggingLokiBasicAuth from a JSON string
config_management_telemetry_logging_loki_basic_auth_instance = ConfigManagementTelemetryLoggingLokiBasicAuth.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetryLoggingLokiBasicAuth.to_json()

# convert the object into a dict
config_management_telemetry_logging_loki_basic_auth_dict = config_management_telemetry_logging_loki_basic_auth_instance.to_dict()
# create an instance of ConfigManagementTelemetryLoggingLokiBasicAuth from a dict
config_management_telemetry_logging_loki_basic_auth_form_dict = config_management_telemetry_logging_loki_basic_auth.from_dict(config_management_telemetry_logging_loki_basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


