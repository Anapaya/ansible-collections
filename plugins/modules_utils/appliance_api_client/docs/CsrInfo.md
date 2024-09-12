# CsrInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**CertificateSubject**](CertificateSubject.md) |  | 
**creation_time** | **datetime** |  | 
**id** | **str** |  | 

## Example

```python
from openapi_client.models.csr_info import CsrInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CsrInfo from a JSON string
csr_info_instance = CsrInfo.from_json(json)
# print the JSON string representation of the object
print CsrInfo.to_json()

# convert the object into a dict
csr_info_dict = csr_info_instance.to_dict()
# create an instance of CsrInfo from a dict
csr_info_form_dict = csr_info.from_dict(csr_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


