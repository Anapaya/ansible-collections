# ScionTunnelingDiscoverySession


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_isd_as** | **str** |  | 
**remote_isd_as** | **str** |  | 
**path** | **str** | SCION path used for the discovery request. | 
**peers** | [**List[ScionTunnelingDiscoveryPeer]**](ScionTunnelingDiscoveryPeer.md) | The list of peers announced by the remote ISD-AS. | 
**last_success** | **str** | The last time when the list of peers was fetched successfully. | [optional] 
**error** | **str** | Error from the last discovery request. If the last request was successful it is not filled in.  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_discovery_session import ScionTunnelingDiscoverySession

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingDiscoverySession from a JSON string
scion_tunneling_discovery_session_instance = ScionTunnelingDiscoverySession.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingDiscoverySession.to_json()

# convert the object into a dict
scion_tunneling_discovery_session_dict = scion_tunneling_discovery_session_instance.to_dict()
# create an instance of ScionTunnelingDiscoverySession from a dict
scion_tunneling_discovery_session_form_dict = scion_tunneling_discovery_session.from_dict(scion_tunneling_discovery_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


