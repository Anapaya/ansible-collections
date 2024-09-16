# ConfigCluster

The configuration for the appliance cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**ConfigClusterFeatures**](ConfigClusterFeatures.md) |  | [optional] 
**peers** | [**List[ConfigClusterPeer]**](ConfigClusterPeer.md) | The list of peers in this cluster. This is used to configure the topology or the discovery of the topology of peer appliances in an organization. | [optional] 
**synchronization** | [**ConfigClusterSynchronization**](ConfigClusterSynchronization.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster import ConfigCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCluster from a JSON string
config_cluster_instance = ConfigCluster.from_json(json)
# print the JSON string representation of the object
print ConfigCluster.to_json()

# convert the object into a dict
config_cluster_dict = config_cluster_instance.to_dict()
# create an instance of ConfigCluster from a dict
config_cluster_form_dict = config_cluster.from_dict(config_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


