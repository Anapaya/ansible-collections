# ConfigExperimentsFeature

The list of features

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the feature | [optional] 
**value** | **str** | The value of the feature | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_experiments_feature import ConfigExperimentsFeature

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigExperimentsFeature from a JSON string
config_experiments_feature_instance = ConfigExperimentsFeature.from_json(json)
# print the JSON string representation of the object
print ConfigExperimentsFeature.to_json()

# convert the object into a dict
config_experiments_feature_dict = config_experiments_feature_instance.to_dict()
# create an instance of ConfigExperimentsFeature from a dict
config_experiments_feature_form_dict = config_experiments_feature.from_dict(config_experiments_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


