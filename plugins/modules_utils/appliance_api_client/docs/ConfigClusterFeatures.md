# ConfigClusterFeatures

The list of feature that are announced to the peers. Note that the actually announced value can depend on whether what features is locally enabled and configured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scion_rss** | **bool** | Option to enable the announcement of support for the SCION RSS feature to the peers. If the local host does not support the SCION RSS feature, this option does not have any effect. | [optional] [default to True]

## Example

```python
from openapi_client.models.config_cluster_features import ConfigClusterFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterFeatures from a JSON string
config_cluster_features_instance = ConfigClusterFeatures.from_json(json)
# print the JSON string representation of the object
print ConfigClusterFeatures.to_json()

# convert the object into a dict
config_cluster_features_dict = config_cluster_features_instance.to_dict()
# create an instance of ConfigClusterFeatures from a dict
config_cluster_features_form_dict = config_cluster_features.from_dict(config_cluster_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


