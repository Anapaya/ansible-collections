# ScionTunnelingSGRPLocalPrefixesJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_prefixes** | [**ScionTunnelingSGRPLocalPrefixes**](ScionTunnelingSGRPLocalPrefixes.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_json import ScionTunnelingSGRPLocalPrefixesJSON

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSGRPLocalPrefixesJSON from a JSON string
scion_tunneling_sgrp_local_prefixes_json_instance = ScionTunnelingSGRPLocalPrefixesJSON.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSGRPLocalPrefixesJSON.to_json()

# convert the object into a dict
scion_tunneling_sgrp_local_prefixes_json_dict = scion_tunneling_sgrp_local_prefixes_json_instance.to_dict()
# create an instance of ScionTunnelingSGRPLocalPrefixesJSON from a dict
scion_tunneling_sgrp_local_prefixes_json_form_dict = scion_tunneling_sgrp_local_prefixes_json.from_dict(scion_tunneling_sgrp_local_prefixes_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


