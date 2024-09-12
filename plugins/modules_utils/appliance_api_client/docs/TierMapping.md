# TierMapping

Describes for each tier what features are allowed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lite** | [**ProductTierFeatures**](ProductTierFeatures.md) |  | [optional] 
**standard** | [**ProductTierFeatures**](ProductTierFeatures.md) |  | [optional] 
**pro** | [**ProductTierFeatures**](ProductTierFeatures.md) |  | [optional] 
**legacy** | [**ProductTierFeatures**](ProductTierFeatures.md) |  | [optional] 

## Example

```python
from openapi_client.models.tier_mapping import TierMapping

# TODO update the JSON string below
json = "{}"
# create an instance of TierMapping from a JSON string
tier_mapping_instance = TierMapping.from_json(json)
# print the JSON string representation of the object
print TierMapping.to_json()

# convert the object into a dict
tier_mapping_dict = tier_mapping_instance.to_dict()
# create an instance of TierMapping from a dict
tier_mapping_form_dict = tier_mapping.from_dict(tier_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


