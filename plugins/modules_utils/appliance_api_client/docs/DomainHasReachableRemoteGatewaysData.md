# DomainHasReachableRemoteGatewaysData

The list of remote Gateways in a domain that are reachable. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain the remote gateways are part of.  | 
**local_isd_as** | **str** | The local ISD-AS in the domain.  | 
**remote_gateways** | [**List[DomainRemoteGateway]**](DomainRemoteGateway.md) | The remote gateways in the domain.  | 

## Example

```python
from openapi_client.models.domain_has_reachable_remote_gateways_data import DomainHasReachableRemoteGatewaysData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainHasReachableRemoteGatewaysData from a JSON string
domain_has_reachable_remote_gateways_data_instance = DomainHasReachableRemoteGatewaysData.from_json(json)
# print the JSON string representation of the object
print DomainHasReachableRemoteGatewaysData.to_json()

# convert the object into a dict
domain_has_reachable_remote_gateways_data_dict = domain_has_reachable_remote_gateways_data_instance.to_dict()
# create an instance of DomainHasReachableRemoteGatewaysData from a dict
domain_has_reachable_remote_gateways_data_form_dict = domain_has_reachable_remote_gateways_data.from_dict(domain_has_reachable_remote_gateways_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


