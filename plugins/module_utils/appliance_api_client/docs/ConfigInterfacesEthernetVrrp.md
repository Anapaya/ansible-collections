# ConfigInterfacesEthernetVrrp

List of VRRP configurations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** | The list of virtual IP addresses. It must contain at least one IP address. Each sequence entry is in CIDR notation. | 
**no_preempt** | **bool** | If set to true, the preempt mode is disabled. This means that the router will not preempt the master even if it has a higher priority than the current master. If set to false, the router will preempt the master if it has a higher priority than the current master. | [optional] [default to False]
**peers** | **List[str]** | Optional list of IP addresses of the VRRP peers. If the list is empty, the router will send VRRP packets to the multicast address. If the list is not empty, the router will send VRRP packets to the unicast addresses specified in the list. | 
**priority** | **int** | The priority value to be used by this VRRP router. Higher means higher priority and it ranges between 1 and 255 (decimal). | [optional] [default to 1]
**vrid** | **int** | The virtual router identifier, which ranges between 1 and 255 (decimal). | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_interfaces_ethernet_vrrp import ConfigInterfacesEthernetVrrp

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesEthernetVrrp from a JSON string
config_interfaces_ethernet_vrrp_instance = ConfigInterfacesEthernetVrrp.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesEthernetVrrp.to_json()

# convert the object into a dict
config_interfaces_ethernet_vrrp_dict = config_interfaces_ethernet_vrrp_instance.to_dict()
# create an instance of ConfigInterfacesEthernetVrrp from a dict
config_interfaces_ethernet_vrrp_form_dict = config_interfaces_ethernet_vrrp.from_dict(config_interfaces_ethernet_vrrp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


