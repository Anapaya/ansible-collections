# LanStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateways** | [**Dict[str, LanStatsGateway]**](LanStatsGateway.md) | A list of local gateways with associated statistics. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.lan_stats import LanStats

# TODO update the JSON string below
json = "{}"
# create an instance of LanStats from a JSON string
lan_stats_instance = LanStats.from_json(json)
# print the JSON string representation of the object
print LanStats.to_json()

# convert the object into a dict
lan_stats_dict = lan_stats_instance.to_dict()
# create an instance of LanStats from a dict
lan_stats_form_dict = lan_stats.from_dict(lan_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


