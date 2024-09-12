# SoftwareLicensesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | **str** | The license as a JSON Web signature. | 

## Example

```python
from openapi_client.models.software_licenses_post_request import SoftwareLicensesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareLicensesPostRequest from a JSON string
software_licenses_post_request_instance = SoftwareLicensesPostRequest.from_json(json)
# print the JSON string representation of the object
print SoftwareLicensesPostRequest.to_json()

# convert the object into a dict
software_licenses_post_request_dict = software_licenses_post_request_instance.to_dict()
# create an instance of SoftwareLicensesPostRequest from a dict
software_licenses_post_request_form_dict = software_licenses_post_request.from_dict(software_licenses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


