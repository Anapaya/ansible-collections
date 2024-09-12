# ConfigScionTunneling

Top-level configuration and state for IP-in-SCION tunneling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[ConfigScionTunnelingDomain]**](ConfigScionTunnelingDomain.md) | List of domains that define the rules by which IP packets are routed. A domain is a subset of the IP space that shares the same policies. | [optional] 
**endpoint** | [**ConfigScionTunnelingEndpoint**](ConfigScionTunnelingEndpoint.md) |  | [optional] 
**path_filters** | [**List[ConfigScionTunnelingPathFilter]**](ConfigScionTunnelingPathFilter.md) | List of path filters that can be referenced by name from a path policies. A path filter defines a set of paths by applying the filter to all available paths. | [optional] 
**remotes** | [**List[ConfigScionTunnelingRemote]**](ConfigScionTunnelingRemote.md) | List of remote ISD-ASes that are connected with the gateway. The remote ISD-ASes can be referenced in the remote matchers of the domains. | [optional] 
**static_announcements** | [**List[ConfigScionTunnelingStaticAnnouncement]**](ConfigScionTunnelingStaticAnnouncement.md) | List of static routes that are advertised. The routes are only advertised to the domains with matching announce filters. | [optional] 
**traffic_matchers** | [**List[ConfigScionTunnelingTrafficMatcher]**](ConfigScionTunnelingTrafficMatcher.md) | List of traffic matchers that can be referenced by name from a traffic policy. A matcher is used to classify traffic for tunneling. Each packet is classified based on configured traffic matchers and put in a traffic class. A traffic class is used in a traffic policy to map a path policy to a traffic class. | [optional] 

## Example

```python
from openapi_client.models.config_scion_tunneling import ConfigScionTunneling

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunneling from a JSON string
config_scion_tunneling_instance = ConfigScionTunneling.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunneling.to_json()

# convert the object into a dict
config_scion_tunneling_dict = config_scion_tunneling_instance.to_dict()
# create an instance of ConfigScionTunneling from a dict
config_scion_tunneling_form_dict = config_scion_tunneling.from_dict(config_scion_tunneling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


