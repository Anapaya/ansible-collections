# ConfigSCIONASNeighborInterfaceRemote

Remote SCION interface endpoint of the link.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | UDP/IP underlay endpoint of the SCION Interface. The data plane traffic is received on this address. The address must be specified as host:port. Both host and port must be specified. | [optional] 
**interface_id** | **int** | SCION interface identifier. It must be unique in the SCION AS. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas_neighbor_interface_remote import ConfigSCIONASNeighborInterfaceRemote

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASNeighborInterfaceRemote from a JSON string
config_scionas_neighbor_interface_remote_instance = ConfigSCIONASNeighborInterfaceRemote.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASNeighborInterfaceRemote.to_json()

# convert the object into a dict
config_scionas_neighbor_interface_remote_dict = config_scionas_neighbor_interface_remote_instance.to_dict()
# create an instance of ConfigSCIONASNeighborInterfaceRemote from a dict
config_scionas_neighbor_interface_remote_form_dict = config_scionas_neighbor_interface_remote.from_dict(config_scionas_neighbor_interface_remote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


