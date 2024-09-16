# ConfigSystemVppTun

TUN configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mtu** | **int** | The MTU (Maximum Transmission Unit) to be used on this TUN. | [optional] [default to 1500]
**prefixes** | **List[str]** | The list of prefixes to route from VPP to Linux. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_vpp_tun import ConfigSystemVppTun

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemVppTun from a JSON string
config_system_vpp_tun_instance = ConfigSystemVppTun.from_json(json)
# print the JSON string representation of the object
print ConfigSystemVppTun.to_json()

# convert the object into a dict
config_system_vpp_tun_dict = config_system_vpp_tun_instance.to_dict()
# create an instance of ConfigSystemVppTun from a dict
config_system_vpp_tun_form_dict = config_system_vpp_tun.from_dict(config_system_vpp_tun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


