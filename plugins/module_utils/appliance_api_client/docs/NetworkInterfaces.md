# NetworkInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | [**List[NetworkInterface]**](NetworkInterface.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.network_interfaces import NetworkInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkInterfaces from a JSON string
network_interfaces_instance = NetworkInterfaces.from_json(json)
# print the JSON string representation of the object
print NetworkInterfaces.to_json()

# convert the object into a dict
network_interfaces_dict = network_interfaces_instance.to_dict()
# create an instance of NetworkInterfaces from a dict
network_interfaces_form_dict = network_interfaces.from_dict(network_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


