# ScionTunnelingDiscoveryPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control** | **str** | Control plane IP address and port. | 
**data** | **str** | Data plane IP address and port. | 
**probe** | **str** | IP address and port used for keepalives. | 
**interfaces** | **List[int]** | A list of SCION interfaces on the remote side to use when accessing this gateway. If not specified, any interface may be used.  | [optional] 

## Example

```python
from openapi_client.models.scion_tunneling_discovery_peer import ScionTunnelingDiscoveryPeer

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingDiscoveryPeer from a JSON string
scion_tunneling_discovery_peer_instance = ScionTunnelingDiscoveryPeer.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingDiscoveryPeer.to_json()

# convert the object into a dict
scion_tunneling_discovery_peer_dict = scion_tunneling_discovery_peer_instance.to_dict()
# create an instance of ScionTunnelingDiscoveryPeer from a dict
scion_tunneling_discovery_peer_form_dict = scion_tunneling_discovery_peer.from_dict(scion_tunneling_discovery_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


