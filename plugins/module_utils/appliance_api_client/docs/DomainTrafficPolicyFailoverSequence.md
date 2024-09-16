# DomainTrafficPolicyFailoverSequence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the failover sequence.  | 
**paths** | **int** | The number of alive paths in the failover sequence.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.domain_traffic_policy_failover_sequence import DomainTrafficPolicyFailoverSequence

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTrafficPolicyFailoverSequence from a JSON string
domain_traffic_policy_failover_sequence_instance = DomainTrafficPolicyFailoverSequence.from_json(json)
# print the JSON string representation of the object
print DomainTrafficPolicyFailoverSequence.to_json()

# convert the object into a dict
domain_traffic_policy_failover_sequence_dict = domain_traffic_policy_failover_sequence_instance.to_dict()
# create an instance of DomainTrafficPolicyFailoverSequence from a dict
domain_traffic_policy_failover_sequence_form_dict = domain_traffic_policy_failover_sequence.from_dict(domain_traffic_policy_failover_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


