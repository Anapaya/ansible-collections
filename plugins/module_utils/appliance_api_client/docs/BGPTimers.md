# BGPTimers

Timers associated with the BGP peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keepalive_interval** | **int** | Time interval in milliseconds between transmission of keepalive messages to the neighbor.  | 
**hold_time** | **int** | Time interval in milliseconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.  | 
**connect_retry** | **int** | Time interval in milliseconds between attempts to establish a session with the peer.  | 
**minimum_advertisement_interval** | **int** | Minimum time in milliseconds which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.bgp_timers import BGPTimers

# TODO update the JSON string below
json = "{}"
# create an instance of BGPTimers from a JSON string
bgp_timers_instance = BGPTimers.from_json(json)
# print the JSON string representation of the object
print BGPTimers.to_json()

# convert the object into a dict
bgp_timers_dict = bgp_timers_instance.to_dict()
# create an instance of BGPTimers from a dict
bgp_timers_form_dict = bgp_timers.from_dict(bgp_timers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


