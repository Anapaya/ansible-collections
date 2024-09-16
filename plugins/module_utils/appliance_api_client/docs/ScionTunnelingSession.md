# ScionTunnelingSession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Unique ID identifying the session. | 
**session_id_legacy** | **int** | Unique ID identifying the session. | 
**local_isd_as** | **str** |  | 
**remote_isd_as** | **str** |  | 
**data_addr** | **str** | IP address and port used to send data to the remote end of the tunnel. | [optional] 
**probe_addr** | **str** | IP address and port used to probe the remote end of the tunnel. | 
**pinned** | **List[int]** | A list of remote SCION interfaces that can be used by this session. If empty, any remote SCION interface can be used.  | 
**domain** | **str** | The domain this session is used to access. | 
**traffic_matcher** | **str** | The class of IP packets this session is used to handle. | 
**path_filter** | **str** | The path filter specifies which SCION paths can be used by this session. | 
**healthy** | **bool** | True if heartbeats are being received from the remote end of the tunnel. | 
**encryption** | [**EncryptionMode**](EncryptionMode.md) |  | 
**paths** | [**List[ScionTunnelingSessionPath]**](ScionTunnelingSessionPath.md) | A list of SCION paths eligible for this session. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_session import ScionTunnelingSession

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSession from a JSON string
scion_tunneling_session_instance = ScionTunnelingSession.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSession.to_json()

# convert the object into a dict
scion_tunneling_session_dict = scion_tunneling_session_instance.to_dict()
# create an instance of ScionTunnelingSession from a dict
scion_tunneling_session_form_dict = scion_tunneling_session.from_dict(scion_tunneling_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


