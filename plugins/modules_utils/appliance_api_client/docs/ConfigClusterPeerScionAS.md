# ConfigClusterPeerScionAS

SCION AS configuration in the peer that is relevant to this appliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control** | [**ConfigClusterPeerScionASControl**](ConfigClusterPeerScionASControl.md) |  | [optional] 
**isd_as** | **str** | ISD-AS number of the AS. | 
**neighbors** | [**List[ConfigClusterPeerScionASNeighbor]**](ConfigClusterPeerScionASNeighbor.md) | The neighbors for the SCION AS in the peer. | [optional] 
**shard_id** | **int** | The shard ID of the peers in the AS. | [optional] 

## Example

```python
from openapi_client.models.config_cluster_peer_scion_as import ConfigClusterPeerScionAS

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScionAS from a JSON string
config_cluster_peer_scion_as_instance = ConfigClusterPeerScionAS.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScionAS.to_json()

# convert the object into a dict
config_cluster_peer_scion_as_dict = config_cluster_peer_scion_as_instance.to_dict()
# create an instance of ConfigClusterPeerScionAS from a dict
config_cluster_peer_scion_as_form_dict = config_cluster_peer_scion_as.from_dict(config_cluster_peer_scion_as_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


