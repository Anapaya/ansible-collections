# CertificateSubject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd_as** | **str** |  | 
**common_name** | **str** | The common name to use in the CSR, may be empty. | [optional] 
**country** | **str** | The 2 letter country code to use in the CSR, may be empty. | [optional] 
**locality** | **str** | The locality to use in the CSR, may be empty. | [optional] 
**organization** | **str** | The organization to use in the CSR, may be empty. | [optional] 
**organizational_unit** | **str** | The organizational unit to use in the CSR, may be empty. | [optional] 
**postal_code** | **str** | The postal code to use in the CSR, may be empty. | [optional] 
**province** | **str** | The province to use in the CSR, may be empty. | [optional] 
**serial_number** | **str** | The serial number to use in the CSR, may be empty. | [optional] 
**street_address** | **str** | The street address to use in the CSR, may be empty. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.certificate_subject import CertificateSubject

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateSubject from a JSON string
certificate_subject_instance = CertificateSubject.from_json(json)
# print the JSON string representation of the object
print CertificateSubject.to_json()

# convert the object into a dict
certificate_subject_dict = certificate_subject_instance.to_dict()
# create an instance of CertificateSubject from a dict
certificate_subject_form_dict = certificate_subject.from_dict(certificate_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


