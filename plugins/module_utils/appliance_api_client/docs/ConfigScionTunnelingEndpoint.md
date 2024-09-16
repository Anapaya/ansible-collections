# ConfigScionTunnelingEndpoint

Local IP-in-SCION tunnel endpoint configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_interfaces** | [**List[ConfigScionTunnelingEndpointAllowedInterfaces]**](ConfigScionTunnelingEndpointAllowedInterfaces.md) | The SCION interfaces for each local SCION AS that are allowed to be used by this IP-in-SCION tunneling endpoint. This can be used to control incoming traffic, e.g., if a tunnel endpoint should only be reachable via SCION interfaces 1 and 2, allowed-interfaces should list them explicitly. Remote tunnel endpoints will then only choose paths entering the respective local AS via SCION interface 1 or 2. If the IP-in-SCION tunneling endpoint on this appliance should be reachable via a SCION interface of a peer appliance, the allowed-interfaces list must be configured with the respective SCION interface of the peer appliance. By default the list is empty, in this case the appliance will automatically configure the locally configured SCION interfaces as allowed-interfaces. Automatic configuration is disabled if topology synchronization is enabled or if disable_auto_allowed_interfaces is set. | [optional] 
**control_port** | **int** | Port number for control traffic. The control address is constructed from the ip address and this control port. The control address is used to exchange IP routing information as part of SGRP. If not set, or zero, the control port will be dynamically allocated. | [optional] 
**data_port** | **int** | Port number for data traffic. The data address is constructed from the ip address and this control port. The data address is used for the IP-in-SCION encapsulated traffic stream. If not set, or zero, the data port will be dynamically allocated. | [optional] 
**description** | **str** | Optional description of the IP-in-SCION tunnel endpoint. | [optional] 
**disable_auto_allowed_interfaces** | **bool** | Whether the automatic configuration of allowed interfaces should be disabled. When disabled, the IP-in-SCION tunneling endpoint will be reached by remote endpoints on all SCION interfaces of the locally configured AS. When enabled (default), the local IP-in-SCION tunneling endpoint will only be reached by remote endpoints on the SCION interfaces that are configured on the local appliance. | [optional] 
**disable_urpf** | **bool** | Flag to disable uRPF. When enabled (default), the gateway performs strict URPF for all the received IP-in-SCION-tunneled traffic, checking that incoming IP packets have a source address that is within the announced prefixes by a remote gateway, and that the SCION packets are sent from a valid remote ISD-AS and are encrypted as configured in the associated domain. | [optional] 
**enable_scion_rss** | **bool** | Flag to activate SCION RSS. If activated, the gateway utilizes UDP source port entropy on the underlay such that sibling routers can leverage RSS for SCION traffic. This can greatly improve throughput performance. This must only be set to true if the routers supports SCION RSS. | [optional] 
**enabled** | **bool** | Whether this endpoint is enabled. | [optional] 
**ip** | **str** | IP address of the local IP-in-SCION endpoint. | [optional] 
**probe_port** | **int** | Port number for probing traffic. The probe address is constructed from the ip address and this probe port. The probe address is used by remote tunnel endpoints in their health probing. If not set, or zero, the probe port will be dynamically allocated. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_endpoint import ConfigScionTunnelingEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingEndpoint from a JSON string
config_scion_tunneling_endpoint_instance = ConfigScionTunnelingEndpoint.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingEndpoint.to_json()

# convert the object into a dict
config_scion_tunneling_endpoint_dict = config_scion_tunneling_endpoint_instance.to_dict()
# create an instance of ConfigScionTunnelingEndpoint from a dict
config_scion_tunneling_endpoint_form_dict = config_scion_tunneling_endpoint.from_dict(config_scion_tunneling_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


