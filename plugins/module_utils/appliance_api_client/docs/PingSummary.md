# PingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | [**Path**](Path.md) |  | 
**payload_size** | **int** | Payload size in bytes | 
**scion_packet_size** | **int** | Packet size in bytes | 
**replies** | [**List[PingUpdate]**](PingUpdate.md) |  | 
**statistics** | [**PingStatistics**](PingStatistics.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.ping_summary import PingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PingSummary from a JSON string
ping_summary_instance = PingSummary.from_json(json)
# print the JSON string representation of the object
print PingSummary.to_json()

# convert the object into a dict
ping_summary_dict = ping_summary_instance.to_dict()
# create an instance of PingSummary from a dict
ping_summary_form_dict = ping_summary.from_dict(ping_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


