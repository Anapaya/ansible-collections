# ConfigClusterPeerScion

The relevant SCION configuration of the peer. This can be used to define the relevant SCION components on the peer appliance so that paths via the peer appliance can also be used.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ases** | [**List[ConfigClusterPeerScionAS]**](ConfigClusterPeerScionAS.md) | The list of SCION ASes on the peer. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion import ConfigClusterPeerScion

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScion from a JSON string
config_cluster_peer_scion_instance = ConfigClusterPeerScion.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScion.to_json()

# convert the object into a dict
config_cluster_peer_scion_dict = config_cluster_peer_scion_instance.to_dict()
# create an instance of ConfigClusterPeerScion from a dict
config_cluster_peer_scion_form_dict = config_cluster_peer_scion.from_dict(config_cluster_peer_scion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


