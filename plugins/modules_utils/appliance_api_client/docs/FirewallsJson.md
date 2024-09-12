# FirewallsJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[FirewallTable]**](FirewallTable.md) | List of firewall tables on the appliance. | 

## Example

```python
from openapi_client.models.firewalls_json import FirewallsJson

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallsJson from a JSON string
firewalls_json_instance = FirewallsJson.from_json(json)
# print the JSON string representation of the object
print FirewallsJson.to_json()

# convert the object into a dict
firewalls_json_dict = firewalls_json_instance.to_dict()
# create an instance of FirewallsJson from a dict
firewalls_json_form_dict = firewalls_json.from_dict(firewalls_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


