# FirewallChain

Firewall chain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the chain. | 
**hook** | **str** | The packet processing step during which the chain should be executed. Must be set for base chains. | [optional] 
**priority** | **int** | The priority of the chain. Must be set for base chains. | [optional] 
**policy** | **str** | The default policy that will be applied to packets that reach the end of the chain.  | [optional] 
**type** | **str** | The type and usage of the chain. Must be set for base chains. | [optional] 
**rules** | [**List[FirewallRule]**](FirewallRule.md) | List of rules that are part of the chain. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.firewall_chain import FirewallChain

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallChain from a JSON string
firewall_chain_instance = FirewallChain.from_json(json)
# print the JSON string representation of the object
print FirewallChain.to_json()

# convert the object into a dict
firewall_chain_dict = firewall_chain_instance.to_dict()
# create an instance of FirewallChain from a dict
firewall_chain_form_dict = firewall_chain.from_dict(firewall_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


