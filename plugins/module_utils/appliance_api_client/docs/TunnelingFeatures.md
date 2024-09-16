# TunnelingFeatures

The tunneling features

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_disallowed** | **bool** | If true, any tunneling configuration is disallowed.  | [optional] 
**max_remotes** | [**MaxOrUnlimited**](MaxOrUnlimited.md) |  | [optional] 
**max_path_filters** | [**MaxOrUnlimited**](MaxOrUnlimited.md) |  | [optional] 
**max_traffic_matchers** | [**MaxOrUnlimited**](MaxOrUnlimited.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.tunneling_features import TunnelingFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelingFeatures from a JSON string
tunneling_features_instance = TunnelingFeatures.from_json(json)
# print the JSON string representation of the object
print TunnelingFeatures.to_json()

# convert the object into a dict
tunneling_features_dict = tunneling_features_instance.to_dict()
# create an instance of TunnelingFeatures from a dict
tunneling_features_form_dict = tunneling_features.from_dict(tunneling_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


