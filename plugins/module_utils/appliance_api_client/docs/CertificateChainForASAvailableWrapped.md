# CertificateChainForASAvailableWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.certificate_chain_for_as_available_wrapped import CertificateChainForASAvailableWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateChainForASAvailableWrapped from a JSON string
certificate_chain_for_as_available_wrapped_instance = CertificateChainForASAvailableWrapped.from_json(json)
# print the JSON string representation of the object
print CertificateChainForASAvailableWrapped.to_json()

# convert the object into a dict
certificate_chain_for_as_available_wrapped_dict = certificate_chain_for_as_available_wrapped_instance.to_dict()
# create an instance of CertificateChainForASAvailableWrapped from a dict
certificate_chain_for_as_available_wrapped_form_dict = certificate_chain_for_as_available_wrapped.from_dict(certificate_chain_for_as_available_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


