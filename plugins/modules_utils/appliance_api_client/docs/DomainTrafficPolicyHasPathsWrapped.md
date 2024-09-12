# DomainTrafficPolicyHasPathsWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from openapi_client.models.domain_traffic_policy_has_paths_wrapped import DomainTrafficPolicyHasPathsWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTrafficPolicyHasPathsWrapped from a JSON string
domain_traffic_policy_has_paths_wrapped_instance = DomainTrafficPolicyHasPathsWrapped.from_json(json)
# print the JSON string representation of the object
print DomainTrafficPolicyHasPathsWrapped.to_json()

# convert the object into a dict
domain_traffic_policy_has_paths_wrapped_dict = domain_traffic_policy_has_paths_wrapped_instance.to_dict()
# create an instance of DomainTrafficPolicyHasPathsWrapped from a dict
domain_traffic_policy_has_paths_wrapped_form_dict = domain_traffic_policy_has_paths_wrapped.from_dict(domain_traffic_policy_has_paths_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


