# ConfigFirewallTableChainRule

List of firewall rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Description, or comment, for the firewall rule. | [optional] 
**rule** | **str** | The rule definition consists of expressions and statements in string format. The expressions are evaluated from left to right and if the packet matches the expressions the statement is executed. For information on the supported syntax for expressions and statements, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Main_Page#Expressions:_Matching_packets and https://wiki.nftables.org/wiki-nftables/index.php/Main_Page#Statements:_Acting_on_packet_matches. | 
**sequence_id** | **int** | The sequence ID determines the order in which sequence the firewall rules are applied. The sequence ID must be unique for each entry. Target devices apply the rules in order of ascending sequence ID (low to high). | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_firewall_table_chain_rule import ConfigFirewallTableChainRule

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFirewallTableChainRule from a JSON string
config_firewall_table_chain_rule_instance = ConfigFirewallTableChainRule.from_json(json)
# print the JSON string representation of the object
print ConfigFirewallTableChainRule.to_json()

# convert the object into a dict
config_firewall_table_chain_rule_dict = config_firewall_table_chain_rule_instance.to_dict()
# create an instance of ConfigFirewallTableChainRule from a dict
config_firewall_table_chain_rule_form_dict = config_firewall_table_chain_rule.from_dict(config_firewall_table_chain_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


