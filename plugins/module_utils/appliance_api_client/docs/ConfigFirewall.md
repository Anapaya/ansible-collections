# ConfigFirewall

The necessary configuration data for firewalling the Anapaya appliance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | The firewall mode declares how the appliance handles firewall rules. Depending on the mode, the appliance either generates a default set of rules, prepends some custom rules, or uses only the specified custom rules. | [optional] 
**tables** | [**List[ConfigFirewallTable]**](ConfigFirewallTable.md) | The list of nftables tables on the Anapaya appliance. The usage of the list depends on the firewall mode. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_firewall import ConfigFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFirewall from a JSON string
config_firewall_instance = ConfigFirewall.from_json(json)
# print the JSON string representation of the object
print ConfigFirewall.to_json()

# convert the object into a dict
config_firewall_dict = config_firewall_instance.to_dict()
# create an instance of ConfigFirewall from a dict
config_firewall_form_dict = config_firewall.from_dict(config_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


