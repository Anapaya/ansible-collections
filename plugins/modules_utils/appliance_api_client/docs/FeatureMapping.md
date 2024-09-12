# FeatureMapping

Describes for each product and tier what features are allowed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge** | [**TierMapping**](TierMapping.md) |  | [optional] 
**core** | [**TierMapping**](TierMapping.md) |  | [optional] 
**gate** | [**TierMapping**](TierMapping.md) |  | [optional] 
**other** | [**TierMapping**](TierMapping.md) |  | [optional] 

## Example

```python
from openapi_client.models.feature_mapping import FeatureMapping

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureMapping from a JSON string
feature_mapping_instance = FeatureMapping.from_json(json)
# print the JSON string representation of the object
print FeatureMapping.to_json()

# convert the object into a dict
feature_mapping_dict = feature_mapping_instance.to_dict()
# create an instance of FeatureMapping from a dict
feature_mapping_form_dict = feature_mapping.from_dict(feature_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


