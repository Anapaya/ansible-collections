# ConfigClusterPeerScionTunneling

The relevant SCION tunneling configuration of the peer. This is used so that all appliances can announce the full list of SCION tunneling endpoints in the AS to other ASes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | [**ConfigClusterPeerScionTunnelingEndpoint**](ConfigClusterPeerScionTunnelingEndpoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.config_cluster_peer_scion_tunneling import ConfigClusterPeerScionTunneling

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScionTunneling from a JSON string
config_cluster_peer_scion_tunneling_instance = ConfigClusterPeerScionTunneling.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScionTunneling.to_json()

# convert the object into a dict
config_cluster_peer_scion_tunneling_dict = config_cluster_peer_scion_tunneling_instance.to_dict()
# create an instance of ConfigClusterPeerScionTunneling from a dict
config_cluster_peer_scion_tunneling_form_dict = config_cluster_peer_scion_tunneling.from_dict(config_cluster_peer_scion_tunneling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


