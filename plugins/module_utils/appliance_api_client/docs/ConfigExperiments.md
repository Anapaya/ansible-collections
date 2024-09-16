# ConfigExperiments

Section for experimental options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[ConfigExperimentsFeature]**](ConfigExperimentsFeature.md) | The list of features. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_experiments import ConfigExperiments

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigExperiments from a JSON string
config_experiments_instance = ConfigExperiments.from_json(json)
# print the JSON string representation of the object
print ConfigExperiments.to_json()

# convert the object into a dict
config_experiments_dict = config_experiments_instance.to_dict()
# create an instance of ConfigExperiments from a dict
config_experiments_form_dict = config_experiments.from_dict(config_experiments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


