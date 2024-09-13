# ManagementFeatures

The management features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_oauth_disallowed** | **bool** | If true, the API OAuth feature is disallowed.  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.management_features import ManagementFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementFeatures from a JSON string
management_features_instance = ManagementFeatures.from_json(json)
# print the JSON string representation of the object
print ManagementFeatures.to_json()

# convert the object into a dict
management_features_dict = management_features_instance.to_dict()
# create an instance of ManagementFeatures from a dict
management_features_form_dict = management_features.from_dict(management_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


