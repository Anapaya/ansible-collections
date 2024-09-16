# ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry

The list of failover sequence entries, each of them associated with a path filter.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_filter** | **str** | Name of the path filter associated with the failover sequence entry. | 
**sequence_id** | **int** | Sequence number of the failover sequence entry. Sequence numbers define  the ordering of the items which turn detemines how the failover  between different path filters happens. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_traffic_policy_failover_sequence_entry import ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry from a JSON string
config_scion_tunneling_domain_traffic_policy_failover_sequence_entry_instance = ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry.to_json()

# convert the object into a dict
config_scion_tunneling_domain_traffic_policy_failover_sequence_entry_dict = config_scion_tunneling_domain_traffic_policy_failover_sequence_entry_instance.to_dict()
# create an instance of ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry from a dict
config_scion_tunneling_domain_traffic_policy_failover_sequence_entry_form_dict = config_scion_tunneling_domain_traffic_policy_failover_sequence_entry.from_dict(config_scion_tunneling_domain_traffic_policy_failover_sequence_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


