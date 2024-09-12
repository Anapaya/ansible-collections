# ProductTierFeatures

Describes the features that are allowed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**management** | [**ManagementFeatures**](ManagementFeatures.md) |  | [optional] 
**scion_tunneling** | [**TunnelingFeatures**](TunnelingFeatures.md) |  | [optional] 
**scion** | [**SCIONFeatures**](SCIONFeatures.md) |  | [optional] 
**lan** | [**LANFeatures**](LANFeatures.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_tier_features import ProductTierFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTierFeatures from a JSON string
product_tier_features_instance = ProductTierFeatures.from_json(json)
# print the JSON string representation of the object
print ProductTierFeatures.to_json()

# convert the object into a dict
product_tier_features_dict = product_tier_features_instance.to_dict()
# create an instance of ProductTierFeatures from a dict
product_tier_features_form_dict = product_tier_features.from_dict(product_tier_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


