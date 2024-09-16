# ConfigSystemVppConnection

Connection configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_check** | [**ConfigSystemVppConnectionHealthCheck**](ConfigSystemVppConnectionHealthCheck.md) |  | [optional] 
**reconnect_attempts** | **int** | The number of connect attempts on start from VPP control services to the VPP dataplane. | [optional] [default to 5]
**reconnect_interval** | **str** | The interval at which a connection is attempted on start from VPP  control services to the VPP dataplane.  It requires a unit suffix out of [&#39;d&#39;, &#39;h&#39;, &#39;m&#39;, &#39;s&#39;, &#39;ms&#39;, &#39;us&#39;, &#39;ns&#39;].  The encoding consists of a decimal number concatenated with a  suffix; for example, &#39;5us&#39;, &#39;10m&#39;, &#39;12h&#39;, and &#39;1d&#39;. | [optional] [default to '1s']

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_vpp_connection import ConfigSystemVppConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemVppConnection from a JSON string
config_system_vpp_connection_instance = ConfigSystemVppConnection.from_json(json)
# print the JSON string representation of the object
print ConfigSystemVppConnection.to_json()

# convert the object into a dict
config_system_vpp_connection_dict = config_system_vpp_connection_instance.to_dict()
# create an instance of ConfigSystemVppConnection from a dict
config_system_vpp_connection_form_dict = config_system_vpp_connection.from_dict(config_system_vpp_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


