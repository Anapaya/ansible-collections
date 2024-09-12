# ScionTunnelingSGRPDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announced** | **List[str]** | Announced IP prefixes in CIDR format. | 
**received** | **List[str]** | Received IP prefixes in CIDR format. | 

## Example

```python
from openapi_client.models.scion_tunneling_sgrp_domain import ScionTunnelingSGRPDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSGRPDomain from a JSON string
scion_tunneling_sgrp_domain_instance = ScionTunnelingSGRPDomain.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSGRPDomain.to_json()

# convert the object into a dict
scion_tunneling_sgrp_domain_dict = scion_tunneling_sgrp_domain_instance.to_dict()
# create an instance of ScionTunnelingSGRPDomain from a dict
scion_tunneling_sgrp_domain_form_dict = scion_tunneling_sgrp_domain.from_dict(scion_tunneling_sgrp_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


