# ConfigClusterPeerScionTunnelingEndpoint

The SCION tunneling endpoint on the peer appliance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_interfaces** | [**List[ConfigClusterPeerScionTunnelingEndpointAllowedInterfaces]**](ConfigClusterPeerScionTunnelingEndpointAllowedInterfaces.md) | The SCION interfaces for each SCION AS that is configured on the peer, that are allowed to be used by this IP-in-SCION tunneling endpoint. This can be used to control incoming traffic, e.g., if a tunnel endpoint should only be reachable via SCION interfaces 1 and 2, allowed-interfaces should list them explicitly. Remote tunnel endpoints will then only choose paths entering the respective local AS via SCION interface 1 or 2. If the IP-in-SCION tunneling endpoint on the peer appliance should be reachable via a SCION interface of another appliance, the allowed-interfaces list must be configured with the respective SCION interfaces. By default the list is empty, in this case the appliance will automatically configure the SCION interfaces that are configured on the peer as allowed-interfaces. Automatic configuration can be disabled by setting disable_auto_allowed_interfaces. | [optional] 
**control_port** | **int** | Port number for control traffic. The control address is constructed from the IP address and this control port. The control address is used to exchange IP routing information as part of SGRP. If not set, or zero, the control port will be dynamically allocated. | [optional] 
**data_port** | **int** | Port number for data traffic. The data address is constructed from the IP address and this control port. The data address is used for the IP-in-SCION encapsulated traffic stream. If not set, or zero, the data port will be dynamically allocated. | [optional] 
**disable_auto_allowed_interfaces** | **bool** | Whether the automatic configuration of allowed interfaces should be disabled. When disabled, the IP-in-SCION tunneling endpoint of the peer will be reached by remote endpoints on all SCION interfaces of the locally configured AS. When enabled (default), the peer IP-in-SCION tunneling endpoint will only be reached by remote endpoints on the SCION interfaces that are configured on the peer appliance. | [optional] 
**ip** | **str** | IP address of the peer IP-in-SCION endpoint. | [optional] 
**probe_port** | **int** | Port number for probing traffic. The probe address is constructed from the IP address and this probe port. The probe address is used by remote tunnel endpoints in their health probing. If not set, or zero, the probe port will be dynamically allocated. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_tunneling_endpoint import ConfigClusterPeerScionTunnelingEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigClusterPeerScionTunnelingEndpoint from a JSON string
config_cluster_peer_scion_tunneling_endpoint_instance = ConfigClusterPeerScionTunnelingEndpoint.from_json(json)
# print the JSON string representation of the object
print ConfigClusterPeerScionTunnelingEndpoint.to_json()

# convert the object into a dict
config_cluster_peer_scion_tunneling_endpoint_dict = config_cluster_peer_scion_tunneling_endpoint_instance.to_dict()
# create an instance of ConfigClusterPeerScionTunnelingEndpoint from a dict
config_cluster_peer_scion_tunneling_endpoint_form_dict = config_cluster_peer_scion_tunneling_endpoint.from_dict(config_cluster_peer_scion_tunneling_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


