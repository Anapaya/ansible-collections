# DebugClusterPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the peer. | 
**address** | **str** | The address of the peer. | 
**last_sync_attempt** | **datetime** | The time of the last synchronization attempt. | 
**status** | **str** | The status of the last synchronization attempt. | 
**error** | **str** | The reason for the failure of the last synchronization. Only present if the status is failure.  | [optional] 

## Example

```python
from openapi_client.models.debug_cluster_peer import DebugClusterPeer

# TODO update the JSON string below
json = "{}"
# create an instance of DebugClusterPeer from a JSON string
debug_cluster_peer_instance = DebugClusterPeer.from_json(json)
# print the JSON string representation of the object
print DebugClusterPeer.to_json()

# convert the object into a dict
debug_cluster_peer_dict = debug_cluster_peer_instance.to_dict()
# create an instance of DebugClusterPeer from a dict
debug_cluster_peer_form_dict = debug_cluster_peer.from_dict(debug_cluster_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


