# FirewallCounter

The firewall named counters definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the named counter. | 
**packets** | **int** | The number of packets the counter has seen. | 
**bytes** | **int** | The number of total bytes the counter has seen. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.firewall_counter import FirewallCounter

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallCounter from a JSON string
firewall_counter_instance = FirewallCounter.from_json(json)
# print the JSON string representation of the object
print FirewallCounter.to_json()

# convert the object into a dict
firewall_counter_dict = firewall_counter_instance.to_dict()
# create an instance of FirewallCounter from a dict
firewall_counter_form_dict = firewall_counter.from_dict(firewall_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


