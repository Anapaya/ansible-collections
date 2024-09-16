# ConfigSCIONASNeighborInterfaceBFD

SCION interface BFD configuration. BFD is used to detect faults on the link to the neighbor AS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_minimum_tx_interval** | **int** | The minimum interval between transmission of BFD control packets that the operator desires. This value is advertised to the peer, however the actual interval used is specified by taking the maximum of desired-minimum-tx-interval and the value of the remote required-minimum-receive interval value. This value is specified as an integer number of microseconds. | [optional] 
**detection_multiplier** | **int** | The number of packets that must be missed to declare this session as down. The detection interval for the BFD session is calculated by multiplying the value of the negotiated transmission interval by this value. | [optional] 
**enabled** | **bool** | If set to true, then the BFD session is enabled on the SCION interface - if it is set to false, BFD is disabled on that SCION interface. When disabled, the health of the interface is not tracked and it is assumed to be healthy. Note that the remote side of this SCION interface should have the same setting for enabled. | [optional] [default to True]
**required_minimum_receive** | **int** | The minimum interval between received BFD control packets that this system should support. This value is advertised to the remote peer to indicate the maximum frequency (i.e., minimum inter-packet interval) between BFD control packets that is acceptable to the local system. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas_neighbor_interface_bfd import ConfigSCIONASNeighborInterfaceBFD

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASNeighborInterfaceBFD from a JSON string
config_scionas_neighbor_interface_bfd_instance = ConfigSCIONASNeighborInterfaceBFD.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASNeighborInterfaceBFD.to_json()

# convert the object into a dict
config_scionas_neighbor_interface_bfd_dict = config_scionas_neighbor_interface_bfd_instance.to_dict()
# create an instance of ConfigSCIONASNeighborInterfaceBFD from a dict
config_scionas_neighbor_interface_bfd_form_dict = config_scionas_neighbor_interface_bfd.from_dict(config_scionas_neighbor_interface_bfd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


