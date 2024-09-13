# FirewallTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the nftables table. | 
**family** | [**FirewallTableFamily**](FirewallTableFamily.md) |  | 
**chains** | [**List[FirewallChain]**](FirewallChain.md) | List of chains in the nftables table. | 
**counters** | [**List[FirewallCounter]**](FirewallCounter.md) | List of named counters in the nftables table. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.firewall_table import FirewallTable

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallTable from a JSON string
firewall_table_instance = FirewallTable.from_json(json)
# print the JSON string representation of the object
print FirewallTable.to_json()

# convert the object into a dict
firewall_table_dict = firewall_table_instance.to_dict()
# create an instance of FirewallTable from a dict
firewall_table_form_dict = firewall_table.from_dict(firewall_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


