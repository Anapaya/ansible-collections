# ConfigManagementTelemetry

Anapaya appliance telemetry configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address where the telemetry data is exposed. This is a combination of an IP address and a fixed port. The address must be specified as host:port, where host can be empty. An empty address indicates a wildcard address. If the address is not specified or the IP is empty and the port is zero, only the management API address exposes the telemetry data. | [optional] 
**flow_metrics** | [**ConfigManagementTelemetryFlowMetrics**](ConfigManagementTelemetryFlowMetrics.md) |  | [optional] 
**labels** | [**List[ConfigManagementTelemetryLabels]**](ConfigManagementTelemetryLabels.md) | List of static labels that are added to all telemetry data (e.g. logs, metrics). | [optional] 
**logging** | [**ConfigManagementTelemetryLogging**](ConfigManagementTelemetryLogging.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_management_telemetry import ConfigManagementTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetry from a JSON string
config_management_telemetry_instance = ConfigManagementTelemetry.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetry.to_json()

# convert the object into a dict
config_management_telemetry_dict = config_management_telemetry_instance.to_dict()
# create an instance of ConfigManagementTelemetry from a dict
config_management_telemetry_form_dict = config_management_telemetry.from_dict(config_management_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


