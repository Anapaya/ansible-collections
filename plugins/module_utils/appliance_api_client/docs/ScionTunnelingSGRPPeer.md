# ScionTunnelingSGRPPeer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_isd_as** | **str** |  | 
**remote_isd_as** | **str** |  | 
**remote_address** | **str** | IP address and port of the remote peer. | 
**announced** | **List[str]** | IP prefixes in CIDR format that will be announced to the remote gateway the next time it asks.  | 
**received** | **List[str]** | IP prefixes in CIDR format received from the remote gateway during the last discovery attempt.  | 
**path** | **str** | SCION path used for the last SGRP request. | [optional] 
**last_received** | **str** | The last time when the prefixes were received from the peer. | 
**error** | **str** | Error from the last prefix discovery request. If there was no error, the field is not present.  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_peer import ScionTunnelingSGRPPeer

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSGRPPeer from a JSON string
scion_tunneling_sgrp_peer_instance = ScionTunnelingSGRPPeer.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSGRPPeer.to_json()

# convert the object into a dict
scion_tunneling_sgrp_peer_dict = scion_tunneling_sgrp_peer_instance.to_dict()
# create an instance of ScionTunnelingSGRPPeer from a dict
scion_tunneling_sgrp_peer_form_dict = scion_tunneling_sgrp_peer.from_dict(scion_tunneling_sgrp_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


