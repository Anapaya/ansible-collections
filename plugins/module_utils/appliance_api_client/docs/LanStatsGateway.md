# LanStatsGateway


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_address** | **str** | IP address and port used to send probes to the gateway. | 
**local_isd_as** | **str** |  | 
**alive** | **bool** | True if probes are replied to by the gateway. | 
**latency** | **float** | The median round-trip latency to the gateway, in milliseconds. | 
**jitter** | **float** | The jitter of the probes to the gateway, in milliseconds. | 
**last_success_time** | **str** |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.lan_stats_gateway import LanStatsGateway

# TODO update the JSON string below
json = "{}"
# create an instance of LanStatsGateway from a JSON string
lan_stats_gateway_instance = LanStatsGateway.from_json(json)
# print the JSON string representation of the object
print LanStatsGateway.to_json()

# convert the object into a dict
lan_stats_gateway_dict = lan_stats_gateway_instance.to_dict()
# create an instance of LanStatsGateway from a dict
lan_stats_gateway_form_dict = lan_stats_gateway.from_dict(lan_stats_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


