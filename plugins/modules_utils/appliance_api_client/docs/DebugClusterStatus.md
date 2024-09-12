# DebugClusterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | The mode of the cluster. | 
**peers** | [**List[DebugClusterPeer]**](DebugClusterPeer.md) |  | [optional] 

## Example

```python
from openapi_client.models.debug_cluster_status import DebugClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DebugClusterStatus from a JSON string
debug_cluster_status_instance = DebugClusterStatus.from_json(json)
# print the JSON string representation of the object
print DebugClusterStatus.to_json()

# convert the object into a dict
debug_cluster_status_dict = debug_cluster_status_instance.to_dict()
# create an instance of DebugClusterStatus from a dict
debug_cluster_status_form_dict = debug_cluster_status.from_dict(debug_cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


