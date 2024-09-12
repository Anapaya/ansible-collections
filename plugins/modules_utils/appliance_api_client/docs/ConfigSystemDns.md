# ConfigSystemDns

Anapaya appliance DNS configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | [**List[ConfigSystemDnsServers]**](ConfigSystemDnsServers.md) | List of DNS servers. | [optional] 

## Example

```python
from openapi_client.models.config_system_dns import ConfigSystemDns

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemDns from a JSON string
config_system_dns_instance = ConfigSystemDns.from_json(json)
# print the JSON string representation of the object
print ConfigSystemDns.to_json()

# convert the object into a dict
config_system_dns_dict = config_system_dns_instance.to_dict()
# create an instance of ConfigSystemDns from a dict
config_system_dns_form_dict = config_system_dns.from_dict(config_system_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


