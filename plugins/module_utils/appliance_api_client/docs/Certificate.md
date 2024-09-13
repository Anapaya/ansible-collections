# Certificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguished_name** | **str** |  | 
**isd_as** | **str** |  | 
**validity** | [**Validity**](Validity.md) |  | 
**subject_key_algo** | **str** |  | 
**subject_key_id** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print Certificate.to_json()

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_form_dict = certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


