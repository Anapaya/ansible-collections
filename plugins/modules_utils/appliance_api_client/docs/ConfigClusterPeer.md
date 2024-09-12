# ConfigClusterPeer

The peer of this appliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Textual description for this peer. | [optional] 
**features** | [**ConfigClusterPeerFeatures**](ConfigClusterPeerFeatures.md) |  | [optional] 
**name** | **str** | The name of this peer used to identify the peer. This can be any string but must be unique among all peers. | [optional] 
**scion** | [**ConfigClusterPeerScion**](ConfigClusterPeerScion.md) |  | [optional] 
**scion_tunneling** | [**ConfigClusterPeerScionTunneling**](ConfigClusterPeerScionTunneling.md) |  | [optional] 
**synchronization** | [**ConfigClusterPeerSynchronization**](ConfigClusterPeerSynchronization.md) |  | [optional] 

## Example

```python
from openapi_client.models.config_cluster_peer import ConfigClusterPeer

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeer from a JSON string
config_cluster_peer_instance = ConfigClusterPeer.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeer.to_json()

# convert the object into a dict
config_cluster_peer_dict = config_cluster_peer_instance.to_dict()
# create an instance of ConfigClusterPeer from a dict
config_cluster_peer_form_dict = config_cluster_peer.from_dict(config_cluster_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


