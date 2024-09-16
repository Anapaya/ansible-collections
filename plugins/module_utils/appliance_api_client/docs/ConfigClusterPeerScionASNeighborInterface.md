# ConfigClusterPeerScionASNeighborInterface

SCION interface that links to the neighbor AS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_id** | **int** | SCION interface identifier. It must be unique in the SCION AS. | 
**next_hop** | **str** | Internal address of the peer router that owns the interface. | [optional] 
**scion_mtu** | **int** | The maximum transmission unit in bytes for SCION packets. This represents the protocol data unit (PDU) of the SCION layer on this interface and is usually calculated as maximum Ethernet payload - IP Header - UDP Header.  | [optional] [default to 1472]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as_neighbor_interface import ConfigClusterPeerScionASNeighborInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScionASNeighborInterface from a JSON string
config_cluster_peer_scion_as_neighbor_interface_instance = ConfigClusterPeerScionASNeighborInterface.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScionASNeighborInterface.to_json()

# convert the object into a dict
config_cluster_peer_scion_as_neighbor_interface_dict = config_cluster_peer_scion_as_neighbor_interface_instance.to_dict()
# create an instance of ConfigClusterPeerScionASNeighborInterface from a dict
config_cluster_peer_scion_as_neighbor_interface_form_dict = config_cluster_peer_scion_as_neighbor_interface.from_dict(config_cluster_peer_scion_as_neighbor_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


