# ConfigSCIONSynchronization

The synchronization configuration contains the configuration for SCION path and beacon synchronization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beacon_synchronization_interval** | **str** | The interval between two consecutive beacon synchronizations attempts to the cluster peers. It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;]. The encoding consists of a decimal number concatenated with a suffix; for example, &#39;5s&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;. | [optional] [default to '4s']
**path_segment_synchronization_interval** | **str** | The interval between two consecutive path segment synchronizations attempts to cluster peers. It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;]. The encoding consists of a decimal number concatenated with a suffix; for example, &#39;5s&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;. | [optional] [default to '4s']

## Example

```python
from openapi_client.models.config_scion_synchronization import ConfigSCIONSynchronization

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONSynchronization from a JSON string
config_scion_synchronization_instance = ConfigSCIONSynchronization.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONSynchronization.to_json()

# convert the object into a dict
config_scion_synchronization_dict = config_scion_synchronization_instance.to_dict()
# create an instance of ConfigSCIONSynchronization from a dict
config_scion_synchronization_form_dict = config_scion_synchronization.from_dict(config_scion_synchronization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


