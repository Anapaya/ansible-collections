# ScionTunnelingDomainsResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[ScionTunnelingDomainConfig]**](ScionTunnelingDomainConfig.md) | A list of the configured SCION tunneling domains. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_domains_response_json import ScionTunnelingDomainsResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingDomainsResponseJson from a JSON string
scion_tunneling_domains_response_json_instance = ScionTunnelingDomainsResponseJson.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingDomainsResponseJson.to_json()

# convert the object into a dict
scion_tunneling_domains_response_json_dict = scion_tunneling_domains_response_json_instance.to_dict()
# create an instance of ScionTunnelingDomainsResponseJson from a dict
scion_tunneling_domains_response_json_form_dict = scion_tunneling_domains_response_json.from_dict(scion_tunneling_domains_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


