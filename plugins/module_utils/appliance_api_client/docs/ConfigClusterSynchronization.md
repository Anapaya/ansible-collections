# ConfigClusterSynchronization

The configuration data necessary for the anapaya cluster synchronization. This determines how frequently this appliance synchronizes its local data with its peers, if synchronization is enabled.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address where peers can fetch topology information. If this is not set, topology information is not exposed to peers and should be statically configured on the peers. | [optional] 
**node_synchronization_interval** | **str** | The interval between two consecutive topology synchronizations attempts to the cluster peers. Must only be set if dynamic topology discovery is enabled. It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;]. The encoding consists of a decimal number concatenated with a suffix; for example, &#39;5s&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;. | [optional] [default to '1m']

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_synchronization import ConfigClusterSynchronization

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterSynchronization from a JSON string
config_cluster_synchronization_instance = ConfigClusterSynchronization.from_json(json)
# print the JSON string representation of the object
print ConfigClusterSynchronization.to_json()

# convert the object into a dict
config_cluster_synchronization_dict = config_cluster_synchronization_instance.to_dict()
# create an instance of ConfigClusterSynchronization from a dict
config_cluster_synchronization_form_dict = config_cluster_synchronization.from_dict(config_cluster_synchronization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


