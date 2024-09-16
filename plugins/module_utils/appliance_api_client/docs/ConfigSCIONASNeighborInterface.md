# ConfigSCIONASNeighborInterface

SCION interface that links to the neighbor AS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | UDP/IP underlay endpoint of the SCION Interface. The data plane traffic is received on this address. The address must be specified as host:port. Both host and port must be specified. | [optional] 
**administrative_state** | **str** | Administrative state of the SCION interface.  Experimental: Currently only UP is supported. | [optional] 
**bfd** | [**ConfigSCIONASNeighborInterfaceBFD**](ConfigSCIONASNeighborInterfaceBFD.md) |  | [optional] 
**description** | **str** | Description, or comment, for the SCION interface. | [optional] 
**enable_scion_rss** | **bool** | Flag to activate SCION RSS for this link. If activated, the router utilizes UDP source port entropy on the underlay such that the remote router can leverage RSS for SCION traffic. This can greatly improve throughput performance. Only enable it if the remote router supports SCION RSS. | [optional] 
**interface_id** | **int** | SCION interface identifier. It must be unique in the SCION AS. | 
**remote** | [**ConfigSCIONASNeighborInterfaceRemote**](ConfigSCIONASNeighborInterfaceRemote.md) |  | [optional] 
**scion_mtu** | **int** | The maximum transmission unit in bytes for SCION packets. This represents the protocol data unit (PDU) of the SCION layer on this interface and is usually calculated as maximum Ethernet payload - IP Header - UDP Header.  | [optional] [default to 1472]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas_neighbor_interface import ConfigSCIONASNeighborInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASNeighborInterface from a JSON string
config_scionas_neighbor_interface_instance = ConfigSCIONASNeighborInterface.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASNeighborInterface.to_json()

# convert the object into a dict
config_scionas_neighbor_interface_dict = config_scionas_neighbor_interface_instance.to_dict()
# create an instance of ConfigSCIONASNeighborInterface from a dict
config_scionas_neighbor_interface_form_dict = config_scionas_neighbor_interface.from_dict(config_scionas_neighbor_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


