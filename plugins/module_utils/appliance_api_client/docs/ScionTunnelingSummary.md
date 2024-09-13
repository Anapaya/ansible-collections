# ScionTunnelingSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[ScionTunnelingSession]**](ScionTunnelingSession.md) | A list of sessions. A session is a tunnel between two SCION appliances with a specific policy governing the selection of SCION paths.  | 
**routing_chains** | [**List[ScionTunnelingRoutingChain]**](ScionTunnelingRoutingChain.md) | A list of routing chains. A routing chain describes how outgoing IP packets are routed to different sessions.  | 
**paths** | [**Dict[str, ScionPathWithMetrics]**](ScionPathWithMetrics.md) | A map of currently used SCION paths, indexed by path fingerprint. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_summary import ScionTunnelingSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSummary from a JSON string
scion_tunneling_summary_instance = ScionTunnelingSummary.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSummary.to_json()

# convert the object into a dict
scion_tunneling_summary_dict = scion_tunneling_summary_instance.to_dict()
# create an instance of ScionTunnelingSummary from a dict
scion_tunneling_summary_form_dict = scion_tunneling_summary.from_dict(scion_tunneling_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


