# ConfigSystemNtpServers

List of NTP servers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of a NTP server. This may be expressed as an IP address or a FQDN. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_ntp_servers import ConfigSystemNtpServers

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemNtpServers from a JSON string
config_system_ntp_servers_instance = ConfigSystemNtpServers.from_json(json)
# print the JSON string representation of the object
print ConfigSystemNtpServers.to_json()

# convert the object into a dict
config_system_ntp_servers_dict = config_system_ntp_servers_instance.to_dict()
# create an instance of ConfigSystemNtpServers from a dict
config_system_ntp_servers_form_dict = config_system_ntp_servers.from_dict(config_system_ntp_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


