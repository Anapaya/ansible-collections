# ScionTunnelingDomainConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The name of the domain. | 
**default** | **bool** | True if the domain is the default domain. | 
**encryption** | [**EncryptionMode**](EncryptionMode.md) |  | 
**local_isd_ases** | **List[str]** | A list of gateway local SCION ISD-ASes. | 
**remote_isd_ases** | [**List[ScionTunnelingIsdAsFilter]**](ScionTunnelingIsdAsFilter.md) | A list of remote SCION ISD-ASes. | 
**prefixes** | [**ScionTunnelingDomainConfigPrefixes**](ScionTunnelingDomainConfigPrefixes.md) |  | 
**traffic_policies** | [**List[ScionTunnelingTrafficPolicy]**](ScionTunnelingTrafficPolicy.md) | A list of traffic policies. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_domain_config import ScionTunnelingDomainConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingDomainConfig from a JSON string
scion_tunneling_domain_config_instance = ScionTunnelingDomainConfig.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingDomainConfig.to_json()

# convert the object into a dict
scion_tunneling_domain_config_dict = scion_tunneling_domain_config_instance.to_dict()
# create an instance of ScionTunnelingDomainConfig from a dict
scion_tunneling_domain_config_form_dict = scion_tunneling_domain_config.from_dict(scion_tunneling_domain_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


