# ConfigClusterPeerScionASNeighbor

Neighbor SCION AS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | [**List[ConfigClusterPeerScionASNeighborInterface]**](ConfigClusterPeerScionASNeighborInterface.md) | The list of interfaces on the peer for this neighbor AS. | [optional] 
**neighbor_isd_as** | **str** | ISD-AS number of the neighbor AS. | 
**relationship** | **str** | The relationship to the neighbor AS. If the local AS is core, this value must either be CORE or CHILD. If the local is non-core, this value must either be PARENT, CHILD or PEER. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as_neighbor import ConfigClusterPeerScionASNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScionASNeighbor from a JSON string
config_cluster_peer_scion_as_neighbor_instance = ConfigClusterPeerScionASNeighbor.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScionASNeighbor.to_json()

# convert the object into a dict
config_cluster_peer_scion_as_neighbor_dict = config_cluster_peer_scion_as_neighbor_instance.to_dict()
# create an instance of ConfigClusterPeerScionASNeighbor from a dict
config_cluster_peer_scion_as_neighbor_form_dict = config_cluster_peer_scion_as_neighbor.from_dict(config_cluster_peer_scion_as_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


