# ConfigScionTunnelingDomainTrafficPolicy

List of traffic policies.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The optional description of the traffic policy. | [optional] 
**failover_sequence** | [**List[ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry]**](ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry.md) | A list of failover sequence entries, each of them associated with a path filter. If there&#39;s no live path left after applying the first filter the second one is tried and so on. | [optional] 
**sequence_id** | **int** | The sequence ID determines the order in which sequence the traffic policies are applied. The sequence ID must be unique for each entry. Target devices try to find the first entry with a matching traffic matcher in ascending order determined by the sequence ID (low to high). | 
**traffic_matcher** | **str** | Reference of the traffic matcher that is utilized by this policy. The traffic matcher is a selector for the IP packets covered by this traffic policy. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_traffic_policy import ConfigScionTunnelingDomainTrafficPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingDomainTrafficPolicy from a JSON string
config_scion_tunneling_domain_traffic_policy_instance = ConfigScionTunnelingDomainTrafficPolicy.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingDomainTrafficPolicy.to_json()

# convert the object into a dict
config_scion_tunneling_domain_traffic_policy_dict = config_scion_tunneling_domain_traffic_policy_instance.to_dict()
# create an instance of ConfigScionTunnelingDomainTrafficPolicy from a dict
config_scion_tunneling_domain_traffic_policy_form_dict = config_scion_tunneling_domain_traffic_policy.from_dict(config_scion_tunneling_domain_traffic_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


