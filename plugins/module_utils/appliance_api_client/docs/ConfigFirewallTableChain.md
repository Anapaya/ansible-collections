# ConfigFirewallTableChain

List of chains that are part of an nftables table, uniquely idenified by their name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chaintype** | **str** | The type and usage of the chain. This must be set for base chains and unset for regular chains. | [optional] 
**hook** | **str** | The packet processing step during which the chain should be executed. This must be set for base chains and unset for regular chains. For more information on the chain hooks, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains#Base_chain_hooks. | [optional] 
**name** | **str** | The name of the chain. | 
**policy** | **str** | The default policy that will be applied to packets that reach the end of the chain. For more information on chain policies, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains#Base_chain_policy. | [optional] 
**priority** | **int** | The priority of the chain. This must be set for base chains and unset for regular chains. | [optional] 
**rules** | [**List[ConfigFirewallTableChainRule]**](ConfigFirewallTableChainRule.md) | Rules defined as part of a chain within a firewall table. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_firewall_table_chain import ConfigFirewallTableChain

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFirewallTableChain from a JSON string
config_firewall_table_chain_instance = ConfigFirewallTableChain.from_json(json)
# print the JSON string representation of the object
print ConfigFirewallTableChain.to_json()

# convert the object into a dict
config_firewall_table_chain_dict = config_firewall_table_chain_instance.to_dict()
# create an instance of ConfigFirewallTableChain from a dict
config_firewall_table_chain_form_dict = config_firewall_table_chain.from_dict(config_firewall_table_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


