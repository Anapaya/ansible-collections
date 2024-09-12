# LANFeatures

The LAN features

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redundancy_disallowed** | **bool** | If true, any LAN redundancy is disallowed.  | [optional] 

## Example

```python
from openapi_client.models.lan_features import LANFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of LANFeatures from a JSON string
lan_features_instance = LANFeatures.from_json(json)
# print the JSON string representation of the object
print LANFeatures.to_json()

# convert the object into a dict
lan_features_dict = lan_features_instance.to_dict()
# create an instance of LANFeatures from a dict
lan_features_form_dict = lan_features.from_dict(lan_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


