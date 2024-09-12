# ConfigSystemDnsServers

List of DNS servers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP address of a DNS server. | [optional] 

## Example

```python
from openapi_client.models.config_system_dns_servers import ConfigSystemDnsServers

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemDnsServers from a JSON string
config_system_dns_servers_instance = ConfigSystemDnsServers.from_json(json)
# print the JSON string representation of the object
print ConfigSystemDnsServers.to_json()

# convert the object into a dict
config_system_dns_servers_dict = config_system_dns_servers_instance.to_dict()
# create an instance of ConfigSystemDnsServers from a dict
config_system_dns_servers_form_dict = config_system_dns_servers.from_dict(config_system_dns_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


