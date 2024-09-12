# DomainTrafficPolicyHasPathsData

The number of paths per failover sequence in a traffic policy in a domain. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain in which the traffic policy is.  | 
**traffic_matcher** | **str** | The name of the traffic matcher that is being checked.  | 
**failover_sequence** | [**List[DomainTrafficPolicyFailoverSequence]**](DomainTrafficPolicyFailoverSequence.md) | The failover sequence that is being checked.  | 

## Example

```python
from openapi_client.models.domain_traffic_policy_has_paths_data import DomainTrafficPolicyHasPathsData

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTrafficPolicyHasPathsData from a JSON string
domain_traffic_policy_has_paths_data_instance = DomainTrafficPolicyHasPathsData.from_json(json)
# print the JSON string representation of the object
print DomainTrafficPolicyHasPathsData.to_json()

# convert the object into a dict
domain_traffic_policy_has_paths_data_dict = domain_traffic_policy_has_paths_data_instance.to_dict()
# create an instance of DomainTrafficPolicyHasPathsData from a dict
domain_traffic_policy_has_paths_data_form_dict = domain_traffic_policy_has_paths_data.from_dict(domain_traffic_policy_has_paths_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


