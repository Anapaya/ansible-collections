# ScionTunnelingSGRPLocalPrefixesStatic

Statically defined prefixes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefixes** | **List[str]** | IP prefixes in CIDR format. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static import ScionTunnelingSGRPLocalPrefixesStatic

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSGRPLocalPrefixesStatic from a JSON string
scion_tunneling_sgrp_local_prefixes_static_instance = ScionTunnelingSGRPLocalPrefixesStatic.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSGRPLocalPrefixesStatic.to_json()

# convert the object into a dict
scion_tunneling_sgrp_local_prefixes_static_dict = scion_tunneling_sgrp_local_prefixes_static_instance.to_dict()
# create an instance of ScionTunnelingSGRPLocalPrefixesStatic from a dict
scion_tunneling_sgrp_local_prefixes_static_form_dict = scion_tunneling_sgrp_local_prefixes_static.from_dict(scion_tunneling_sgrp_local_prefixes_static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


