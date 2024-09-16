# ConfigSystemVpp

Anapaya appliance VPP configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buffers** | [**ConfigSystemVppBuffers**](ConfigSystemVppBuffers.md) |  | [optional] 
**connection** | [**ConfigSystemVppConnection**](ConfigSystemVppConnection.md) |  | [optional] 
**cpu** | [**ConfigSystemVppCpu**](ConfigSystemVppCpu.md) |  | [optional] 
**poll_sleep** | **str** | The fixed-sleep between main loop polls in the VPP dataplane.  It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;, &#39;ms&#39;, &#39;us&#39;, &#39;ns&#39;].  The encoding consists of a decimal number concatenated with a  suffix; for example, &#39;5us&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;.  Setting it to 0 disables the fixed-sleep. | [optional] [default to '0s']
**tun** | [**ConfigSystemVppTun**](ConfigSystemVppTun.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_vpp import ConfigSystemVpp

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemVpp from a JSON string
config_system_vpp_instance = ConfigSystemVpp.from_json(json)
# print the JSON string representation of the object
print ConfigSystemVpp.to_json()

# convert the object into a dict
config_system_vpp_dict = config_system_vpp_instance.to_dict()
# create an instance of ConfigSystemVpp from a dict
config_system_vpp_form_dict = config_system_vpp.from_dict(config_system_vpp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


