# FeatureSetMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the feature set mapping. | 
**feature_mapping** | [**FeatureMapping**](FeatureMapping.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.feature_set_mapping import FeatureSetMapping

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureSetMapping from a JSON string
feature_set_mapping_instance = FeatureSetMapping.from_json(json)
# print the JSON string representation of the object
print FeatureSetMapping.to_json()

# convert the object into a dict
feature_set_mapping_dict = feature_set_mapping_instance.to_dict()
# create an instance of FeatureSetMapping from a dict
feature_set_mapping_form_dict = feature_set_mapping.from_dict(feature_set_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


