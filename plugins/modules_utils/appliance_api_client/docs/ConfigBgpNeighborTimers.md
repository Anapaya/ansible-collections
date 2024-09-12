# ConfigBgpNeighborTimers

Timers related to a BGP neighbor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_retry** | **int** | Time interval in seconds between attempts to establish a session with the peer. | [optional] [default to 30]
**hold_time** | **int** | Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.    The hold-time is typically set to 3x the keepalive-interval. | [optional] [default to 30]
**keepalive_interval** | **int** | Time interval in seconds between transmission of keepalive messages to the neighbor.    Typically set to 1/3 the hold-time. | [optional] [default to 10]
**minimum_advertisement_interval** | **int** | Minimum time in seconds which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability. | [optional] [default to 30]

## Example

```python
from openapi_client.models.config_bgp_neighbor_timers import ConfigBgpNeighborTimers

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigBgpNeighborTimers from a JSON string
config_bgp_neighbor_timers_instance = ConfigBgpNeighborTimers.from_json(json)
# print the JSON string representation of the object
print ConfigBgpNeighborTimers.to_json()

# convert the object into a dict
config_bgp_neighbor_timers_dict = config_bgp_neighbor_timers_instance.to_dict()
# create an instance of ConfigBgpNeighborTimers from a dict
config_bgp_neighbor_timers_form_dict = config_bgp_neighbor_timers.from_dict(config_bgp_neighbor_timers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


