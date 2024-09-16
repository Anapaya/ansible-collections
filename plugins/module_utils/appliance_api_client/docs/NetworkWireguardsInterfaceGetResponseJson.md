# NetworkWireguardsInterfaceGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**public_key** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.network_wireguards_interface_get_response_json import NetworkWireguardsInterfaceGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkWireguardsInterfaceGetResponseJson from a JSON string
network_wireguards_interface_get_response_json_instance = NetworkWireguardsInterfaceGetResponseJson.from_json(json)
# print the JSON string representation of the object
print NetworkWireguardsInterfaceGetResponseJson.to_json()

# convert the object into a dict
network_wireguards_interface_get_response_json_dict = network_wireguards_interface_get_response_json_instance.to_dict()
# create an instance of NetworkWireguardsInterfaceGetResponseJson from a dict
network_wireguards_interface_get_response_json_form_dict = network_wireguards_interface_get_response_json.from_dict(network_wireguards_interface_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


