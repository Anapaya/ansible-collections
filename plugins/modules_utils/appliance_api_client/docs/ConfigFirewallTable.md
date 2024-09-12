# ConfigFirewallTable

List of nftables tables that should be configured on the local system, uniquely identified by their name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chains** | [**List[ConfigFirewallTableChain]**](ConfigFirewallTableChain.md) | Chains defined within the nftables table. | [optional] 
**counters** | [**List[ConfigFirewallTableCounter]**](ConfigFirewallTableCounter.md) | Optional named counters defined within the nftables table. | [optional] 
**family** | **str** | The family type of the nftables. For more information on table families, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Nftables_families. | [optional] 
**name** | **str** | Name of the nftables table. | 

## Example

```python
from openapi_client.models.config_firewall_table import ConfigFirewallTable

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFirewallTable from a JSON string
config_firewall_table_instance = ConfigFirewallTable.from_json(json)
# print the JSON string representation of the object
print ConfigFirewallTable.to_json()

# convert the object into a dict
config_firewall_table_dict = config_firewall_table_instance.to_dict()
# create an instance of ConfigFirewallTable from a dict
config_firewall_table_form_dict = config_firewall_table.from_dict(config_firewall_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


