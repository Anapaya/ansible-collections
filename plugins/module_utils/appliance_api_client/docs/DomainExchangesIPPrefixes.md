# DomainExchangesIPPrefixes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DomainExchangesIPPrefixesData**](DomainExchangesIPPrefixesData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_exchanges_ip_prefixes import DomainExchangesIPPrefixes

# TODO update the JSON string below
json = "{}"
# create an instance of DomainExchangesIPPrefixes from a JSON string
domain_exchanges_ip_prefixes_instance = DomainExchangesIPPrefixes.from_json(json)
# print the JSON string representation of the object
print DomainExchangesIPPrefixes.to_json()

# convert the object into a dict
domain_exchanges_ip_prefixes_dict = domain_exchanges_ip_prefixes_instance.to_dict()
# create an instance of DomainExchangesIPPrefixes from a dict
domain_exchanges_ip_prefixes_form_dict = domain_exchanges_ip_prefixes.from_dict(domain_exchanges_ip_prefixes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


