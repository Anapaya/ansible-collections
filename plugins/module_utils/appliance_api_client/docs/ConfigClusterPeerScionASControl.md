# ConfigClusterPeerScionASControl

Configuration and state data for the control service in the peer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address of the control service. The address must be specified as host:port. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_as_control import ConfigClusterPeerScionASControl

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScionASControl from a JSON string
config_cluster_peer_scion_as_control_instance = ConfigClusterPeerScionASControl.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScionASControl.to_json()

# convert the object into a dict
config_cluster_peer_scion_as_control_dict = config_cluster_peer_scion_as_control_instance.to_dict()
# create an instance of ConfigClusterPeerScionASControl from a dict
config_cluster_peer_scion_as_control_form_dict = config_cluster_peer_scion_as_control.from_dict(config_cluster_peer_scion_as_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


