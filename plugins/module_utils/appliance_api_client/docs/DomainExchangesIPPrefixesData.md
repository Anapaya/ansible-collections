# DomainExchangesIPPrefixesData

Indicates the number of accepted prefixes from remote gateways and the number of announced prefixes.  If either received or announced or both are zero, the status is `notice`. Otherwise, the status is `passing`. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of the routing domain.  | 
**received_prefixes** | **int** | The number of received IP prefixes that pass the accept filters.  | 
**announced_prefixes** | **int** | The number of announced IP prefixes that pass the announce filters.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_exchanges_ip_prefixes_data import DomainExchangesIPPrefixesData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainExchangesIPPrefixesData from a JSON string
domain_exchanges_ip_prefixes_data_instance = DomainExchangesIPPrefixesData.from_json(json)
# print the JSON string representation of the object
print DomainExchangesIPPrefixesData.to_json()

# convert the object into a dict
domain_exchanges_ip_prefixes_data_dict = domain_exchanges_ip_prefixes_data_instance.to_dict()
# create an instance of DomainExchangesIPPrefixesData from a dict
domain_exchanges_ip_prefixes_data_form_dict = domain_exchanges_ip_prefixes_data.from_dict(domain_exchanges_ip_prefixes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


