# SoftwareLicenseFeaturesPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **str** | The feature set as a JSON Web signature. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.software_license_features_put_request import SoftwareLicenseFeaturesPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareLicenseFeaturesPutRequest from a JSON string
software_license_features_put_request_instance = SoftwareLicenseFeaturesPutRequest.from_json(json)
# print the JSON string representation of the object
print SoftwareLicenseFeaturesPutRequest.to_json()

# convert the object into a dict
software_license_features_put_request_dict = software_license_features_put_request_instance.to_dict()
# create an instance of SoftwareLicenseFeaturesPutRequest from a dict
software_license_features_put_request_form_dict = software_license_features_put_request.from_dict(software_license_features_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


