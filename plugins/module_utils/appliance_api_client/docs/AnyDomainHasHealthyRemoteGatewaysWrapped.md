# AnyDomainHasHealthyRemoteGatewaysWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.any_domain_has_healthy_remote_gateways_wrapped import AnyDomainHasHealthyRemoteGatewaysWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of AnyDomainHasHealthyRemoteGatewaysWrapped from a JSON string
any_domain_has_healthy_remote_gateways_wrapped_instance = AnyDomainHasHealthyRemoteGatewaysWrapped.from_json(json)
# print the JSON string representation of the object
print AnyDomainHasHealthyRemoteGatewaysWrapped.to_json()

# convert the object into a dict
any_domain_has_healthy_remote_gateways_wrapped_dict = any_domain_has_healthy_remote_gateways_wrapped_instance.to_dict()
# create an instance of AnyDomainHasHealthyRemoteGatewaysWrapped from a dict
any_domain_has_healthy_remote_gateways_wrapped_form_dict = any_domain_has_healthy_remote_gateways_wrapped.from_dict(any_domain_has_healthy_remote_gateways_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


