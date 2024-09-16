# ConfigSystemVppConnectionHealthCheck

Health check configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_interval** | **str** | The interval in which a health check probe is sent to the VPP dataplane.  It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;, &#39;ms&#39;, &#39;us&#39;, &#39;ns&#39;].  The encoding consists of a decimal number concatenated with a  suffix; for example, &#39;5us&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;. | [optional] [default to '1s']
**reply_timeout** | **str** | The time in which VPP control services expect a reply from the VPP dataplane.  It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;, &#39;ms&#39;, &#39;us&#39;, &#39;ns&#39;].  The encoding consists of a decimal number concatenated with a  suffix; for example, &#39;5us&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;. | [optional] [default to '250ms']
**threshold** | **int** | The number of health checks, from VPP control services to the VPP dataplane, that are allowed to time out before the connection is considered dead. | [optional] [default to 3]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_vpp_connection_health_check import ConfigSystemVppConnectionHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemVppConnectionHealthCheck from a JSON string
config_system_vpp_connection_health_check_instance = ConfigSystemVppConnectionHealthCheck.from_json(json)
# print the JSON string representation of the object
print ConfigSystemVppConnectionHealthCheck.to_json()

# convert the object into a dict
config_system_vpp_connection_health_check_dict = config_system_vpp_connection_health_check_instance.to_dict()
# create an instance of ConfigSystemVppConnectionHealthCheck from a dict
config_system_vpp_connection_health_check_form_dict = config_system_vpp_connection_health_check.from_dict(config_system_vpp_connection_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


