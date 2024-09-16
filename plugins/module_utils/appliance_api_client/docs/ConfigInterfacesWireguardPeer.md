# ConfigInterfacesWireguardPeer

List of Wireguard peer configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_ips** | **List[str]** | A list of IPv4/IPv6 addresses with a CIDR mask. The list indicates the addresses from which the peer is allowed to connect. Catch all are expressed as 0.0.0.0/0 (IPv4) and ::/0 (IPv6) | [optional] 
**endpoint** | **str** | Remote endpoint of the Wireguard tunnel. In the form &#x60;host:port&#x60; where &#x60;host&#x60; can be an IPv4/IPv6 address or a hostname, and &#x60;port&#x60; is a port number. | 
**public_key** | **str** | The base64 encoded public key of the Wireguard peer. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_wireguard_peer import ConfigInterfacesWireguardPeer

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesWireguardPeer from a JSON string
config_interfaces_wireguard_peer_instance = ConfigInterfacesWireguardPeer.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesWireguardPeer.to_json()

# convert the object into a dict
config_interfaces_wireguard_peer_dict = config_interfaces_wireguard_peer_instance.to_dict()
# create an instance of ConfigInterfacesWireguardPeer from a dict
config_interfaces_wireguard_peer_form_dict = config_interfaces_wireguard_peer.from_dict(config_interfaces_wireguard_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


