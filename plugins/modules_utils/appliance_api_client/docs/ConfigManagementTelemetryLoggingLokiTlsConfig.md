# ConfigManagementTelemetryLoggingLokiTlsConfig

Configuration for TLS connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insecure_skip_verify** | **bool** | insecure-skip-verify controls whether the client verifies the Loki server&#39;s certificate chain and host name. If insecure-skip-verify is true, the appliance accepts any certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to machine-in-the-middle attacks unless custom verification is used. This should be used only for testing. | [optional] [default to False]

## Example

```python
from openapi_client.models.config_management_telemetry_logging_loki_tls_config import ConfigManagementTelemetryLoggingLokiTlsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetryLoggingLokiTlsConfig from a JSON string
config_management_telemetry_logging_loki_tls_config_instance = ConfigManagementTelemetryLoggingLokiTlsConfig.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetryLoggingLokiTlsConfig.to_json()

# convert the object into a dict
config_management_telemetry_logging_loki_tls_config_dict = config_management_telemetry_logging_loki_tls_config_instance.to_dict()
# create an instance of ConfigManagementTelemetryLoggingLokiTlsConfig from a dict
config_management_telemetry_logging_loki_tls_config_form_dict = config_management_telemetry_logging_loki_tls_config.from_dict(config_management_telemetry_logging_loki_tls_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


