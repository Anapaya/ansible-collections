# ConfigBgpNeighbor

List of BGP neighbors configured on the local system, uniquely identified by peer IPv4 or IPv6 address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_password** | **str** | An MD5 authentication password for use with the neighboring device. | [optional] 
**bfd** | [**ConfigBgpNeighborBfd**](ConfigBgpNeighborBfd.md) |  | [optional] 
**description** | **str** | An optional textual description of the neighbor. | [optional] 
**ebgp_multihop** | **int** | Specifying ebgp-multihop allows sessions with eBGP neighbors to establish when they are multiple hops away. When the neighbor is not directly connected and this setting is not enabled, the session will not establish. | [optional] 
**enabled** | **bool** | Whether the BGP peer is enabled. In cases where the enabled leaf is set to false, the local system will not initiate connections to the neighbor, and will not respond to TCP connections attempts from the neighbor. If the BGP session is established at the time that this property is set to false, the session will be ceased. | [optional] [default to True]
**local_as** | **int** | The local BGP autonomous system number that is to be used when establishing sessions with the remote peer or peer group, if this differs from the global BGP router autonomous system number. | [optional] 
**neighbor_address** | **str** | Address of the BGP peer, either IPv4 or IPv6. | [optional] 
**peer_as** | **int** | BGP autonomous system number of the peer. | [optional] 
**timers** | [**ConfigBgpNeighborTimers**](ConfigBgpNeighborTimers.md) |  | [optional] 
**transport** | [**ConfigBgpNeighborTransport**](ConfigBgpNeighborTransport.md) |  | [optional] 
**ttl_security** | **int** | BGP Time To Live (TTL) security check. Reference: RFC 5082: The Generalized TTL Security Mechanism (GTSM), RFC 7454: BGP Operations and Security. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_bgp_neighbor import ConfigBgpNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigBgpNeighbor from a JSON string
config_bgp_neighbor_instance = ConfigBgpNeighbor.from_json(json)
# print the JSON string representation of the object
print ConfigBgpNeighbor.to_json()

# convert the object into a dict
config_bgp_neighbor_dict = config_bgp_neighbor_instance.to_dict()
# create an instance of ConfigBgpNeighbor from a dict
config_bgp_neighbor_form_dict = config_bgp_neighbor.from_dict(config_bgp_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


