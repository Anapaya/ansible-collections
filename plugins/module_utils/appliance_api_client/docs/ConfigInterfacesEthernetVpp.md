# ConfigInterfacesEthernetVpp

The VPP driver specific configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_strip_offload** | **bool** | Whether &#x60;vlan-strip-offload on&#x60; should be added to the interface configuration of the VPP dataplane. | [optional] [default to False]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_ethernet_vpp import ConfigInterfacesEthernetVpp

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesEthernetVpp from a JSON string
config_interfaces_ethernet_vpp_instance = ConfigInterfacesEthernetVpp.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesEthernetVpp.to_json()

# convert the object into a dict
config_interfaces_ethernet_vpp_dict = config_interfaces_ethernet_vpp_instance.to_dict()
# create an instance of ConfigInterfacesEthernetVpp from a dict
config_interfaces_ethernet_vpp_form_dict = config_interfaces_ethernet_vpp.from_dict(config_interfaces_ethernet_vpp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


