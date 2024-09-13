# ConfigFirewallTableCounter

List of named counters that are part of an nftables table, uniquely idenified by their name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the counter. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_firewall_table_counter import ConfigFirewallTableCounter

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFirewallTableCounter from a JSON string
config_firewall_table_counter_instance = ConfigFirewallTableCounter.from_json(json)
# print the JSON string representation of the object
print ConfigFirewallTableCounter.to_json()

# convert the object into a dict
config_firewall_table_counter_dict = config_firewall_table_counter_instance.to_dict()
# create an instance of ConfigFirewallTableCounter from a dict
config_firewall_table_counter_form_dict = config_firewall_table_counter.from_dict(config_firewall_table_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


