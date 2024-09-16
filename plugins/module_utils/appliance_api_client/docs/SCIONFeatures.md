# SCIONFeatures

The SCION features

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_ases** | [**MaxOrUnlimited**](MaxOrUnlimited.md) |  | [optional] 
**max_parent_links** | [**MaxOrUnlimited**](MaxOrUnlimited.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_features import SCIONFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of SCIONFeatures from a JSON string
scion_features_instance = SCIONFeatures.from_json(json)
# print the JSON string representation of the object
print SCIONFeatures.to_json()

# convert the object into a dict
scion_features_dict = scion_features_instance.to_dict()
# create an instance of SCIONFeatures from a dict
scion_features_form_dict = scion_features.from_dict(scion_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


