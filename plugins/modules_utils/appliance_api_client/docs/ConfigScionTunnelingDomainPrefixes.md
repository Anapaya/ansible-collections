# ConfigScionTunnelingDomainPrefixes

List of IP prefix matchers to filter the announced and received prefixes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_filter** | [**List[ConfigScionTunnelingDomainPrefixesAcceptFilterEntry]**](ConfigScionTunnelingDomainPrefixesAcceptFilterEntry.md) | List of IP prefix matchers to define which prefixes announced by remotes ISD ASes are accepted. Only the matching subset of a prefix announced by a remote ISD-AS is is accepted for routing. | [optional] 
**announce_filter** | [**List[ConfigScionTunnelingDomainPrefixesAnnounceFilterEntry]**](ConfigScionTunnelingDomainPrefixesAnnounceFilterEntry.md) | List of IP prefix matchers to filter prefixes announced to remotes. The prefixes to be announced are configured in the static announcements or BGP. Only the subset of the routes that matches the announce filter is advertised to the remotes. | [optional] 

## Example

```python
from openapi_client.models.config_scion_tunneling_domain_prefixes import ConfigScionTunnelingDomainPrefixes

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingDomainPrefixes from a JSON string
config_scion_tunneling_domain_prefixes_instance = ConfigScionTunnelingDomainPrefixes.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingDomainPrefixes.to_json()

# convert the object into a dict
config_scion_tunneling_domain_prefixes_dict = config_scion_tunneling_domain_prefixes_instance.to_dict()
# create an instance of ConfigScionTunnelingDomainPrefixes from a dict
config_scion_tunneling_domain_prefixes_form_dict = config_scion_tunneling_domain_prefixes.from_dict(config_scion_tunneling_domain_prefixes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


