# DomainExchangesIPPrefixesWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from openapi_client.models.domain_exchanges_ip_prefixes_wrapped import DomainExchangesIPPrefixesWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of DomainExchangesIPPrefixesWrapped from a JSON string
domain_exchanges_ip_prefixes_wrapped_instance = DomainExchangesIPPrefixesWrapped.from_json(json)
# print the JSON string representation of the object
print DomainExchangesIPPrefixesWrapped.to_json()

# convert the object into a dict
domain_exchanges_ip_prefixes_wrapped_dict = domain_exchanges_ip_prefixes_wrapped_instance.to_dict()
# create an instance of DomainExchangesIPPrefixesWrapped from a dict
domain_exchanges_ip_prefixes_wrapped_form_dict = domain_exchanges_ip_prefixes_wrapped.from_dict(domain_exchanges_ip_prefixes_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


