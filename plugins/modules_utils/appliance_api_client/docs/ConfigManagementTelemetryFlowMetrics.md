# ConfigManagementTelemetryFlowMetrics

Configuration for the flow-metrics feature. The gateway collects information about outgoing flows, such as the source and destination ISD-AS and IP address, in order to export then number of gateway users. The flow information is sent to the flow-collector for storage and processing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanup_task_interval** | **str** | Time interval at which expired flows are cleaned up. | [optional] [default to '60s']
**collector_url** | **str** | URL of the flow-collector where the flow metric information is sent to. Supports &#39;http&#39;, &#39;https&#39; and &#39;grpc&#39; transport | [optional] 
**enabled** | **bool** | Whether the feature is enabled. | [optional] [default to False]
**export_task_interval** | **str** | Time interval at which flow metrics are exported to the collector. | [optional] [default to '60s']
**flow_expiration_interval** | **str** | Time interval after which inactive flows are considered expired and are marked for cleanup. | [optional] [default to '180s']
**proxy_url** | **str** | URL of the optional HTTP(S) proxy. If set, the flow metric information is sent to the collector via the proxy. | [optional] 

## Example

```python
from openapi_client.models.config_management_telemetry_flow_metrics import ConfigManagementTelemetryFlowMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetryFlowMetrics from a JSON string
config_management_telemetry_flow_metrics_instance = ConfigManagementTelemetryFlowMetrics.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetryFlowMetrics.to_json()

# convert the object into a dict
config_management_telemetry_flow_metrics_dict = config_management_telemetry_flow_metrics_instance.to_dict()
# create an instance of ConfigManagementTelemetryFlowMetrics from a dict
config_management_telemetry_flow_metrics_form_dict = config_management_telemetry_flow_metrics.from_dict(config_management_telemetry_flow_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


