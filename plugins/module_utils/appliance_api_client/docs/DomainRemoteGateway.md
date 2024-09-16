# DomainRemoteGateway

A remote gateway instance in a domain. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd_as** | **str** | The ISD-AS of the remote gateway.  | 
**address** | **str** | The address of the remote gateway in the form host:port.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_remote_gateway import DomainRemoteGateway

# TODO update the JSON string below
json = "{}"
# create an instance of DomainRemoteGateway from a JSON string
domain_remote_gateway_instance = DomainRemoteGateway.from_json(json)
# print the JSON string representation of the object
print DomainRemoteGateway.to_json()

# convert the object into a dict
domain_remote_gateway_dict = domain_remote_gateway_instance.to_dict()
# create an instance of DomainRemoteGateway from a dict
domain_remote_gateway_form_dict = domain_remote_gateway.from_dict(domain_remote_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


