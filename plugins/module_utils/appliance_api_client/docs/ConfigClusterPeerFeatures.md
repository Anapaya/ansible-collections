# ConfigClusterPeerFeatures

Configures the feature options of the peer. This field can not be set together with the synchronization field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scion_rss** | **bool** | Option to statically enable the SCION RSS feature. If set to true, the local router enables UDP source port entropy on the underlay for SCION packets forwarded to the peer, such that the peer can leverage RSS for SCION traffic. This can greatly improve throughput performance. This must only be set to true if the peer supports the SCION RSS feature. | [optional] [default to False]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_features import ConfigClusterPeerFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerFeatures from a JSON string
config_cluster_peer_features_instance = ConfigClusterPeerFeatures.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerFeatures.to_json()

# convert the object into a dict
config_cluster_peer_features_dict = config_cluster_peer_features_instance.to_dict()
# create an instance of ConfigClusterPeerFeatures from a dict
config_cluster_peer_features_form_dict = config_cluster_peer_features.from_dict(config_cluster_peer_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


