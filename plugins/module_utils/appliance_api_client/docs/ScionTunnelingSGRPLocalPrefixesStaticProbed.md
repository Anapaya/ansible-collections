# ScionTunnelingSGRPLocalPrefixesStaticProbed

Statically defined prefixes with probing. The prefixes are announced only if the next hop address is reachable. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_hop** | **str** | IP address to probe. | 
**reachable** | **bool** | If true, the next hop address is reachable and the prefixes are announced to the peers.  | 
**last_success** | **str** | The last time when the next hop address was successfully probed. | 
**prefixes** | **List[str]** | IP prefixes in CIDR format. | 
**error** | **str** | Error from the last ping. If there was no error, the field is not present.  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_static_probed import ScionTunnelingSGRPLocalPrefixesStaticProbed

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSGRPLocalPrefixesStaticProbed from a JSON string
scion_tunneling_sgrp_local_prefixes_static_probed_instance = ScionTunnelingSGRPLocalPrefixesStaticProbed.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSGRPLocalPrefixesStaticProbed.to_json()

# convert the object into a dict
scion_tunneling_sgrp_local_prefixes_static_probed_dict = scion_tunneling_sgrp_local_prefixes_static_probed_instance.to_dict()
# create an instance of ScionTunnelingSGRPLocalPrefixesStaticProbed from a dict
scion_tunneling_sgrp_local_prefixes_static_probed_form_dict = scion_tunneling_sgrp_local_prefixes_static_probed.from_dict(scion_tunneling_sgrp_local_prefixes_static_probed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


