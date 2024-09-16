# ConfigClusterPeerSynchronization

The synchronization configuration for this peer. This can be used to configure the automatic synchronization of topology information and supported features. Automatic synchronization of topology and supported features is not recommended for EDGE deployments. Instead static configuration is recommended. This field can not be set together with the scion, scion-tunneling, and features field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The gRPC address of this peer, used for synchronization of appliance information | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_synchronization import ConfigClusterPeerSynchronization

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerSynchronization from a JSON string
config_cluster_peer_synchronization_instance = ConfigClusterPeerSynchronization.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerSynchronization.to_json()

# convert the object into a dict
config_cluster_peer_synchronization_dict = config_cluster_peer_synchronization_instance.to_dict()
# create an instance of ConfigClusterPeerSynchronization from a dict
config_cluster_peer_synchronization_form_dict = config_cluster_peer_synchronization.from_dict(config_cluster_peer_synchronization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


