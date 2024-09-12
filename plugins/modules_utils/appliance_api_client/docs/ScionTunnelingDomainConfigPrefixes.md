# ScionTunnelingDomainConfigPrefixes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announce_filter** | [**List[ScionTunnelingPrefixesFilter]**](ScionTunnelingPrefixesFilter.md) | A list of announced prefixes. | 
**accept_filter** | [**List[ScionTunnelingPrefixesFilter]**](ScionTunnelingPrefixesFilter.md) | A list of accepted prefixes. | 

## Example

```python
from openapi_client.models.scion_tunneling_domain_config_prefixes import ScionTunnelingDomainConfigPrefixes

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingDomainConfigPrefixes from a JSON string
scion_tunneling_domain_config_prefixes_instance = ScionTunnelingDomainConfigPrefixes.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingDomainConfigPrefixes.to_json()

# convert the object into a dict
scion_tunneling_domain_config_prefixes_dict = scion_tunneling_domain_config_prefixes_instance.to_dict()
# create an instance of ScionTunnelingDomainConfigPrefixes from a dict
scion_tunneling_domain_config_prefixes_form_dict = scion_tunneling_domain_config_prefixes.from_dict(scion_tunneling_domain_config_prefixes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


