# ConfigScionTunnelingDomain

List of domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Whether this domain is the default domain. The default domain is assumed to accept the whole IP space that is not covered by other domains. Because of this it may not specify an accept-filter. | [optional] 
**description** | **str** | Optional description, or comment, for the domain. | [optional] 
**local_isd_ases** | **List[str]** | List of local ISD-AS identifiers that belong to this domain. Traffic towards remote ISD-ASes is guaranteed to only use paths that start at one of these local ISD-ASes. | [optional] 
**name** | **str** | The name of the domain. | 
**prefixes** | [**ConfigScionTunnelingDomainPrefixes**](ConfigScionTunnelingDomainPrefixes.md) |  | [optional] 
**remote_isd_ases** | [**List[ConfigScionTunnelingDomainRemoteMatcher]**](ConfigScionTunnelingDomainRemoteMatcher.md) | List of remote ISD-AS identifiers that belong to this domain. Prefix announcements will be accepted from these remote ISD-ASes. All IP traffic will be tunneled over paths that end in one of these remote ISD-ASes. | [optional] 
**traffic_policies** | [**List[ConfigScionTunnelingDomainTrafficPolicy]**](ConfigScionTunnelingDomainTrafficPolicy.md) | List of traffic policies that configure the types of traffic that are tunneled via this domain and the tunnel properties. A traffic policy defines a matcher on the IP traffic (the traffic matcher). If the IP traffic matches, it is tunneled to the remote SCION AS. Acceptable paths for the tunnel are defined via the path policy | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain import ConfigScionTunnelingDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingDomain from a JSON string
config_scion_tunneling_domain_instance = ConfigScionTunnelingDomain.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingDomain.to_json()

# convert the object into a dict
config_scion_tunneling_domain_dict = config_scion_tunneling_domain_instance.to_dict()
# create an instance of ConfigScionTunnelingDomain from a dict
config_scion_tunneling_domain_form_dict = config_scion_tunneling_domain.from_dict(config_scion_tunneling_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


