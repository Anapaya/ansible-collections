# ScionPathPerformanceMetrics

Performance Metrics of SCION path.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latency** | **float** | The latency of the path, in milliseconds. | 
**jitter** | **float** | The jitter of the path, in milliseconds. | 
**droprate** | **float** | The drop rate of the path, percent. | 
**throughput_pkts** | **float** | The outgoing throughput of the path in packets per second. | 
**throughput_bytes** | **float** | The outgoing throughput of the path in bytes per second. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_path_performance_metrics import ScionPathPerformanceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ScionPathPerformanceMetrics from a JSON string
scion_path_performance_metrics_instance = ScionPathPerformanceMetrics.from_json(json)
# print the JSON string representation of the object
print ScionPathPerformanceMetrics.to_json()

# convert the object into a dict
scion_path_performance_metrics_dict = scion_path_performance_metrics_instance.to_dict()
# create an instance of ScionPathPerformanceMetrics from a dict
scion_path_performance_metrics_form_dict = scion_path_performance_metrics.from_dict(scion_path_performance_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


