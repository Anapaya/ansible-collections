# ConfigInterfacesWireguard

List of Wireguard interfaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The addresses configured on this interface. Each address must be a valid IP prefix in CIDR notation. | [optional] 
**gateway** | [**ConfigInterfacesWireguardGateway**](ConfigInterfacesWireguardGateway.md) |  | [optional] 
**mtu** | **int** | The MTU (Maximum Transmission Unit) to be used on this interface. | [optional] [default to 1420]
**name** | **str** | The name of the network interface. | 
**peers** | [**List[ConfigInterfacesWireguardPeer]**](ConfigInterfacesWireguardPeer.md) | The list of Wireguard peers. | [optional] 
**pointopoint** | **str** | This enables the point-to-point mode on the interface, meaning that it is a direct link between two machines with nobody else listening on it. | [optional] 
**port** | **int** | The port to listen on. | 
**routes** | [**List[ConfigInterfacesWireguardRoute]**](ConfigInterfacesWireguardRoute.md) | The routes for the network interface. | [optional] 

## Example

```python
from openapi_client.models.config_interfaces_wireguard import ConfigInterfacesWireguard

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesWireguard from a JSON string
config_interfaces_wireguard_instance = ConfigInterfacesWireguard.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesWireguard.to_json()

# convert the object into a dict
config_interfaces_wireguard_dict = config_interfaces_wireguard_instance.to_dict()
# create an instance of ConfigInterfacesWireguard from a dict
config_interfaces_wireguard_form_dict = config_interfaces_wireguard.from_dict(config_interfaces_wireguard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


