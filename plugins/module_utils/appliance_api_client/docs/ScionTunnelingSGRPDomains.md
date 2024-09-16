# ScionTunnelingSGRPDomains


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**Dict[str, ScionTunnelingSGRPDomain]**](ScionTunnelingSGRPDomain.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_domains import ScionTunnelingSGRPDomains

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSGRPDomains from a JSON string
scion_tunneling_sgrp_domains_instance = ScionTunnelingSGRPDomains.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSGRPDomains.to_json()

# convert the object into a dict
scion_tunneling_sgrp_domains_dict = scion_tunneling_sgrp_domains_instance.to_dict()
# create an instance of ScionTunnelingSGRPDomains from a dict
scion_tunneling_sgrp_domains_form_dict = scion_tunneling_sgrp_domains.from_dict(scion_tunneling_sgrp_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


