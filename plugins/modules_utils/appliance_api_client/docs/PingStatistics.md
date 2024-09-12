# PingStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | **int** | Total number of packets sent | 
**received** | **int** | Total number of packets received | 
**packet_loss** | **float** | Total number of dropped packets | 
**time** | **int** | Total runtime in ms | 

## Example

```python
from openapi_client.models.ping_statistics import PingStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PingStatistics from a JSON string
ping_statistics_instance = PingStatistics.from_json(json)
# print the JSON string representation of the object
print PingStatistics.to_json()

# convert the object into a dict
ping_statistics_dict = ping_statistics_instance.to_dict()
# create an instance of PingStatistics from a dict
ping_statistics_form_dict = ping_statistics.from_dict(ping_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


