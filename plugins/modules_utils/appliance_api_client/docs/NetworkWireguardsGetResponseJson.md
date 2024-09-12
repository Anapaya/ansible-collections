# NetworkWireguardsGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | [**List[NetworkWireguardsInterfaceGetResponseJson]**](NetworkWireguardsInterfaceGetResponseJson.md) | List of wireguard interfaces | 

## Example

```python
from openapi_client.models.network_wireguards_get_response_json import NetworkWireguardsGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkWireguardsGetResponseJson from a JSON string
network_wireguards_get_response_json_instance = NetworkWireguardsGetResponseJson.from_json(json)
# print the JSON string representation of the object
print NetworkWireguardsGetResponseJson.to_json()

# convert the object into a dict
network_wireguards_get_response_json_dict = network_wireguards_get_response_json_instance.to_dict()
# create an instance of NetworkWireguardsGetResponseJson from a dict
network_wireguards_get_response_json_form_dict = network_wireguards_get_response_json.from_dict(network_wireguards_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


