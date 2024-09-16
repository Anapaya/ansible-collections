# ansible.module_utils.appliance_api_client.VppApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_debug_vpp_address**](VppApi.md#get_debug_vpp_address) | **GET** /debug/vpp/address | Status page listing addresses on VPP interfaces.
[**get_debug_vpp_bfd**](VppApi.md#get_debug_vpp_bfd) | **GET** /debug/vpp/bfd | Status page reporting the bfd session states.
[**get_debug_vpp_bond**](VppApi.md#get_debug_vpp_bond) | **GET** /debug/vpp/bond | Status page reporting bonds created by VPP.
[**get_debug_vpp_buffers**](VppApi.md#get_debug_vpp_buffers) | **GET** /debug/vpp/buffers | Status page reporting VPP buffers.
[**get_debug_vpp_clear_errors**](VppApi.md#get_debug_vpp_clear_errors) | **GET** /debug/vpp/clear_errors | Action path to clear VPP errors.
[**get_debug_vpp_clear_interfaces**](VppApi.md#get_debug_vpp_clear_interfaces) | **GET** /debug/vpp/clear_interfaces | Action path to clear the metrics on VPP interfaces.
[**get_debug_vpp_clear_runtime**](VppApi.md#get_debug_vpp_clear_runtime) | **GET** /debug/vpp/clear_runtime | Action path to clear the VPP runtime.
[**get_debug_vpp_coredump**](VppApi.md#get_debug_vpp_coredump) | **GET** /debug/vpp/coredumps/{filename} | Download the coredump.
[**get_debug_vpp_coredumps**](VppApi.md#get_debug_vpp_coredumps) | **GET** /debug/vpp/coredumps | Get the list of avaiable VPP coredumps.
[**get_debug_vpp_dataplane_control**](VppApi.md#get_debug_vpp_dataplane_control) | **GET** /debug/vpp/dataplane-control | Dump of the VPP state set up by dataplane-control service.
[**get_debug_vpp_error**](VppApi.md#get_debug_vpp_error) | **GET** /debug/vpp/error | Status page reporting VPP errors.
[**get_debug_vpp_events**](VppApi.md#get_debug_vpp_events) | **GET** /debug/vpp/events | Status page reporting VPP events.
[**get_debug_vpp_fib_ip4**](VppApi.md#get_debug_vpp_fib_ip4) | **GET** /debug/vpp/fib-ip4 | Status page reporting VPP IPv4 FIB.
[**get_debug_vpp_fib_ip6**](VppApi.md#get_debug_vpp_fib_ip6) | **GET** /debug/vpp/fib-ip6 | Status page reporting VPP IPv6 FIB.
[**get_debug_vpp_fib_ll**](VppApi.md#get_debug_vpp_fib_ll) | **GET** /debug/vpp/fib-ll | Status page reporting VPP IPv6 link-local FIB.
[**get_debug_vpp_gateway**](VppApi.md#get_debug_vpp_gateway) | **GET** /debug/vpp/gateway | Dump of the VPP state set up by the gateway service.
[**get_debug_vpp_hardware**](VppApi.md#get_debug_vpp_hardware) | **GET** /debug/vpp/hardware | Status page listing hardware interfaces managed by VPP.
[**get_debug_vpp_interface**](VppApi.md#get_debug_vpp_interface) | **GET** /debug/vpp/interface | Status page listing internal VPP interfaces.
[**get_debug_vpp_lacp**](VppApi.md#get_debug_vpp_lacp) | **GET** /debug/vpp/lacp | Status page reporting VPP LACP info.
[**get_debug_vpp_lcp**](VppApi.md#get_debug_vpp_lcp) | **GET** /debug/vpp/lcp | Status page listing interfaces mirrored from VPP to Linux.
[**get_debug_vpp_logging**](VppApi.md#get_debug_vpp_logging) | **GET** /debug/vpp/logging | Status page reporting VPP logs.
[**get_debug_vpp_memory**](VppApi.md#get_debug_vpp_memory) | **GET** /debug/vpp/memory | Status page reporting VPP memory.
[**get_debug_vpp_neighbors_ip4**](VppApi.md#get_debug_vpp_neighbors_ip4) | **GET** /debug/vpp/neighbors-ip4 | Status page reporting VPP IPv4 neighbors.
[**get_debug_vpp_neighbors_ip6**](VppApi.md#get_debug_vpp_neighbors_ip6) | **GET** /debug/vpp/neighbors-ip6 | Status page reporting VPP IPv6 neighbors.
[**get_debug_vpp_plugins**](VppApi.md#get_debug_vpp_plugins) | **GET** /debug/vpp/plugins | Status page listing of loaded VPP plugins.
[**get_debug_vpp_runtime**](VppApi.md#get_debug_vpp_runtime) | **GET** /debug/vpp/runtime | Status page reporting VPP runtime.
[**get_debug_vpp_scion_interface**](VppApi.md#get_debug_vpp_scion_interface) | **GET** /debug/vpp/scion/interface | Status page reporting the SCION interfaces.
[**get_debug_vpp_scion_ipfix_params**](VppApi.md#get_debug_vpp_scion_ipfix_params) | **GET** /debug/vpp/scion/ipfix/params | Status page reporting the SCION router IPFIX parameters.
[**get_debug_vpp_scion_ipfix_statistics**](VppApi.md#get_debug_vpp_scion_ipfix_statistics) | **GET** /debug/vpp/scion/ipfix/statistics | Status page reporting the SCION router IPFIX statistics.
[**get_debug_vpp_scion_ipfix_table**](VppApi.md#get_debug_vpp_scion_ipfix_table) | **GET** /debug/vpp/scion/ipfix/table | Status page reporting the SCION router IPFIX table.
[**get_debug_vpp_scion_isd_as**](VppApi.md#get_debug_vpp_scion_isd_as) | **GET** /debug/vpp/scion/isd-as | Status page reporting the SCION router ASes.
[**get_debug_vpp_scion_reservation**](VppApi.md#get_debug_vpp_scion_reservation) | **GET** /debug/vpp/scion/reservation | Status page reporting the SCION router bandwidth reservations.
[**get_debug_vpp_scion_svc**](VppApi.md#get_debug_vpp_scion_svc) | **GET** /debug/vpp/scion/svc | Status page reporting the SCION services.
[**get_debug_vpp_scion_tunneling_decap_to_output**](VppApi.md#get_debug_vpp_scion_tunneling_decap_to_output) | **GET** /debug/vpp/scion-tunneling/decap-to-output | SCION gateway: trace all ingress IP packets.
[**get_debug_vpp_scion_tunneling_dpdk_to_decap**](VppApi.md#get_debug_vpp_scion_tunneling_dpdk_to_decap) | **GET** /debug/vpp/scion-tunneling/dpdk-to-decap | SCION gateway: trace all ingress frames entering via dpdk.
[**get_debug_vpp_scion_tunneling_dpdk_to_encap4**](VppApi.md#get_debug_vpp_scion_tunneling_dpdk_to_encap4) | **GET** /debug/vpp/scion-tunneling/dpdk-to-encap4 | SCION gateway: trace all egress IPv4 packets entering via dpdk.
[**get_debug_vpp_scion_tunneling_dpdk_to_encap6**](VppApi.md#get_debug_vpp_scion_tunneling_dpdk_to_encap6) | **GET** /debug/vpp/scion-tunneling/dpdk-to-encap6 | SCION gateway: trace all egress IPv6 packets entering via dpdk.
[**get_debug_vpp_scion_tunneling_encap4_to_output**](VppApi.md#get_debug_vpp_scion_tunneling_encap4_to_output) | **GET** /debug/vpp/scion-tunneling/encap4-to-output | SCION gateway: trace all egress frames on top of IPv4 underlay.
[**get_debug_vpp_scion_tunneling_encap6_to_output**](VppApi.md#get_debug_vpp_scion_tunneling_encap6_to_output) | **GET** /debug/vpp/scion-tunneling/encap6-to-output | SCION gateway: trace all egress frames on top of IPv6 underlay.
[**get_debug_vpp_scion_tunneling_info**](VppApi.md#get_debug_vpp_scion_tunneling_info) | **GET** /debug/vpp/scion-tunneling/info | SCION gateway: global settings.
[**get_debug_vpp_scion_tunneling_iremote_ia**](VppApi.md#get_debug_vpp_scion_tunneling_iremote_ia) | **GET** /debug/vpp/scion-tunneling/iremote-ia | SCION gateway: remote ASes.
[**get_debug_vpp_scion_tunneling_memif_to_decap**](VppApi.md#get_debug_vpp_scion_tunneling_memif_to_decap) | **GET** /debug/vpp/scion-tunneling/memif-to-decap | SCION gateway: trace all ingress frames entering via memif.
[**get_debug_vpp_scion_tunneling_memif_to_encap4**](VppApi.md#get_debug_vpp_scion_tunneling_memif_to_encap4) | **GET** /debug/vpp/scion-tunneling/memif-to-encap4 | SCION gateway: trace all egress IPv4 packets entering via memif.
[**get_debug_vpp_scion_tunneling_memif_to_encap6**](VppApi.md#get_debug_vpp_scion_tunneling_memif_to_encap6) | **GET** /debug/vpp/scion-tunneling/memif-to-encap6 | SCION gateway: trace all egress IPv6 packets entering via memif.
[**get_debug_vpp_scion_tunneling_path**](VppApi.md#get_debug_vpp_scion_tunneling_path) | **GET** /debug/vpp/scion-tunneling/path | SCION gateway: known paths.
[**get_debug_vpp_scion_tunneling_routing**](VppApi.md#get_debug_vpp_scion_tunneling_routing) | **GET** /debug/vpp/scion-tunneling/routing | SCION gateway: routing hierarchy.
[**get_debug_vpp_scion_tunneling_routing_chain**](VppApi.md#get_debug_vpp_scion_tunneling_routing_chain) | **GET** /debug/vpp/scion-tunneling/routing-chain | SCION gateway: routing chains.
[**get_debug_vpp_scion_tunneling_session**](VppApi.md#get_debug_vpp_scion_tunneling_session) | **GET** /debug/vpp/scion-tunneling/session | SCION gateway: sessions.
[**get_debug_vpp_scion_tunneling_traffic_class**](VppApi.md#get_debug_vpp_scion_tunneling_traffic_class) | **GET** /debug/vpp/scion-tunneling/traffic-class | SCION gateway: traffic classes.
[**get_debug_vpp_scion_tunneling_tun**](VppApi.md#get_debug_vpp_scion_tunneling_tun) | **GET** /debug/vpp/scion-tunneling/tun | SCION gateway: TUN device.
[**get_debug_vpp_trace**](VppApi.md#get_debug_vpp_trace) | **GET** /debug/vpp/trace | Action path to execute free form packet trace.
[**get_debug_vpp_trace_dpdk**](VppApi.md#get_debug_vpp_trace_dpdk) | **GET** /debug/vpp/trace/dpdk | Action path to execute a trace for packets entering via DPDK.
[**get_debug_vpp_trace_memif**](VppApi.md#get_debug_vpp_trace_memif) | **GET** /debug/vpp/trace/memif | Action path to execute a trace for packets entering via memif.
[**get_debug_vpp_trace_start**](VppApi.md#get_debug_vpp_trace_start) | **GET** /debug/vpp/trace/start | Action path that starts a trace without timeout. The trace can be stopped with the &#x60;/vpp/trace/stop&#x60; endpoint.
[**get_debug_vpp_trace_stop**](VppApi.md#get_debug_vpp_trace_stop) | **GET** /debug/vpp/trace/stop | Action path that stops tracing.
[**get_debug_vpp_trace_udp4_socket**](VppApi.md#get_debug_vpp_trace_udp4_socket) | **GET** /debug/vpp/trace/udp4-socket | Action path to execute a trace for IPv4 packets entering via VPP UDP socket.
[**get_debug_vpp_trace_udp6_socket**](VppApi.md#get_debug_vpp_trace_udp6_socket) | **GET** /debug/vpp/trace/udp6-socket | Action path to execute a trace for IPv6 packets entering via VPP UDP socket.
[**get_debug_vpp_trace_virtio**](VppApi.md#get_debug_vpp_trace_virtio) | **GET** /debug/vpp/trace/virtio | Action path to execute a trace for packets entering via TUN/TAP.
[**get_debug_vpp_tun**](VppApi.md#get_debug_vpp_tun) | **GET** /debug/vpp/tun | Status page reporting TUN/TAP devices created by VPP.
[**get_debug_vpp_vrrp**](VppApi.md#get_debug_vpp_vrrp) | **GET** /debug/vpp/vrrp | Status page reporting VPP VRRP.


# **get_debug_vpp_address**
> str get_debug_vpp_address()

Status page listing addresses on VPP interfaces.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page listing addresses on VPP interfaces.
        api_response = api_instance.get_debug_vpp_address()
        print("The response of VppApi->get_debug_vpp_address:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_address: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_bfd**
> str get_debug_vpp_bfd()

Status page reporting the bfd session states.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the bfd session states.
        api_response = api_instance.get_debug_vpp_bfd()
        print("The response of VppApi->get_debug_vpp_bfd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_bfd: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_bond**
> str get_debug_vpp_bond()

Status page reporting bonds created by VPP.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting bonds created by VPP.
        api_response = api_instance.get_debug_vpp_bond()
        print("The response of VppApi->get_debug_vpp_bond:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_bond: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_buffers**
> str get_debug_vpp_buffers()

Status page reporting VPP buffers.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP buffers.
        api_response = api_instance.get_debug_vpp_buffers()
        print("The response of VppApi->get_debug_vpp_buffers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_buffers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_clear_errors**
> str get_debug_vpp_clear_errors()

Action path to clear VPP errors.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Action path to clear VPP errors.
        api_response = api_instance.get_debug_vpp_clear_errors()
        print("The response of VppApi->get_debug_vpp_clear_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_clear_errors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_clear_interfaces**
> str get_debug_vpp_clear_interfaces()

Action path to clear the metrics on VPP interfaces.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Action path to clear the metrics on VPP interfaces.
        api_response = api_instance.get_debug_vpp_clear_interfaces()
        print("The response of VppApi->get_debug_vpp_clear_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_clear_interfaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_clear_runtime**
> str get_debug_vpp_clear_runtime()

Action path to clear the VPP runtime.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Action path to clear the VPP runtime.
        api_response = api_instance.get_debug_vpp_clear_runtime()
        print("The response of VppApi->get_debug_vpp_clear_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_clear_runtime: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_coredump**
> List[str] get_debug_vpp_coredump(filename)

Download the coredump.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    filename = 'filename_example' # str | Filename of the coredump.

    try:
        # Download the coredump.
        api_response = api_instance.get_debug_vpp_coredump(filename)
        print("The response of VppApi->get_debug_vpp_coredump:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_coredump: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| Filename of the coredump. | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available VPP coredumps. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_coredumps**
> List[str] get_debug_vpp_coredumps()

Get the list of avaiable VPP coredumps.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Get the list of avaiable VPP coredumps.
        api_response = api_instance.get_debug_vpp_coredumps()
        print("The response of VppApi->get_debug_vpp_coredumps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_coredumps: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available VPP coredumps. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_dataplane_control**
> object get_debug_vpp_dataplane_control()

Dump of the VPP state set up by dataplane-control service.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Dump of the VPP state set up by dataplane-control service.
        api_response = api_instance.get_debug_vpp_dataplane_control()
        print("The response of VppApi->get_debug_vpp_dataplane_control:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_dataplane_control: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dump of the VPP internal state. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_error**
> str get_debug_vpp_error()

Status page reporting VPP errors.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP errors.
        api_response = api_instance.get_debug_vpp_error()
        print("The response of VppApi->get_debug_vpp_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_error: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_events**
> str get_debug_vpp_events()

Status page reporting VPP events.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP events.
        api_response = api_instance.get_debug_vpp_events()
        print("The response of VppApi->get_debug_vpp_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_fib_ip4**
> str get_debug_vpp_fib_ip4()

Status page reporting VPP IPv4 FIB.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP IPv4 FIB.
        api_response = api_instance.get_debug_vpp_fib_ip4()
        print("The response of VppApi->get_debug_vpp_fib_ip4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_fib_ip4: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_fib_ip6**
> str get_debug_vpp_fib_ip6()

Status page reporting VPP IPv6 FIB.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP IPv6 FIB.
        api_response = api_instance.get_debug_vpp_fib_ip6()
        print("The response of VppApi->get_debug_vpp_fib_ip6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_fib_ip6: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_fib_ll**
> str get_debug_vpp_fib_ll()

Status page reporting VPP IPv6 link-local FIB.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP IPv6 link-local FIB.
        api_response = api_instance.get_debug_vpp_fib_ll()
        print("The response of VppApi->get_debug_vpp_fib_ll:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_fib_ll: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_gateway**
> object get_debug_vpp_gateway()

Dump of the VPP state set up by the gateway service.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Dump of the VPP state set up by the gateway service.
        api_response = api_instance.get_debug_vpp_gateway()
        print("The response of VppApi->get_debug_vpp_gateway:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_gateway: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dump of the VPP internal state. |  -  |
**500** | Internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_hardware**
> str get_debug_vpp_hardware()

Status page listing hardware interfaces managed by VPP.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page listing hardware interfaces managed by VPP.
        api_response = api_instance.get_debug_vpp_hardware()
        print("The response of VppApi->get_debug_vpp_hardware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_hardware: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_interface**
> str get_debug_vpp_interface()

Status page listing internal VPP interfaces.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page listing internal VPP interfaces.
        api_response = api_instance.get_debug_vpp_interface()
        print("The response of VppApi->get_debug_vpp_interface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_interface: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_lacp**
> str get_debug_vpp_lacp()

Status page reporting VPP LACP info.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP LACP info.
        api_response = api_instance.get_debug_vpp_lacp()
        print("The response of VppApi->get_debug_vpp_lacp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_lacp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_lcp**
> str get_debug_vpp_lcp()

Status page listing interfaces mirrored from VPP to Linux.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page listing interfaces mirrored from VPP to Linux.
        api_response = api_instance.get_debug_vpp_lcp()
        print("The response of VppApi->get_debug_vpp_lcp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_lcp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_logging**
> str get_debug_vpp_logging()

Status page reporting VPP logs.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP logs.
        api_response = api_instance.get_debug_vpp_logging()
        print("The response of VppApi->get_debug_vpp_logging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_logging: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_memory**
> str get_debug_vpp_memory()

Status page reporting VPP memory.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP memory.
        api_response = api_instance.get_debug_vpp_memory()
        print("The response of VppApi->get_debug_vpp_memory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_memory: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_neighbors_ip4**
> str get_debug_vpp_neighbors_ip4()

Status page reporting VPP IPv4 neighbors.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP IPv4 neighbors.
        api_response = api_instance.get_debug_vpp_neighbors_ip4()
        print("The response of VppApi->get_debug_vpp_neighbors_ip4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_neighbors_ip4: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_neighbors_ip6**
> str get_debug_vpp_neighbors_ip6()

Status page reporting VPP IPv6 neighbors.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP IPv6 neighbors.
        api_response = api_instance.get_debug_vpp_neighbors_ip6()
        print("The response of VppApi->get_debug_vpp_neighbors_ip6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_neighbors_ip6: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_plugins**
> str get_debug_vpp_plugins()

Status page listing of loaded VPP plugins.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page listing of loaded VPP plugins.
        api_response = api_instance.get_debug_vpp_plugins()
        print("The response of VppApi->get_debug_vpp_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_runtime**
> str get_debug_vpp_runtime()

Status page reporting VPP runtime.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP runtime.
        api_response = api_instance.get_debug_vpp_runtime()
        print("The response of VppApi->get_debug_vpp_runtime:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_runtime: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_interface**
> str get_debug_vpp_scion_interface()

Status page reporting the SCION interfaces.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION interfaces.
        api_response = api_instance.get_debug_vpp_scion_interface()
        print("The response of VppApi->get_debug_vpp_scion_interface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_interface: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_ipfix_params**
> str get_debug_vpp_scion_ipfix_params()

Status page reporting the SCION router IPFIX parameters.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION router IPFIX parameters.
        api_response = api_instance.get_debug_vpp_scion_ipfix_params()
        print("The response of VppApi->get_debug_vpp_scion_ipfix_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_ipfix_params: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_ipfix_statistics**
> str get_debug_vpp_scion_ipfix_statistics()

Status page reporting the SCION router IPFIX statistics.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION router IPFIX statistics.
        api_response = api_instance.get_debug_vpp_scion_ipfix_statistics()
        print("The response of VppApi->get_debug_vpp_scion_ipfix_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_ipfix_statistics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_ipfix_table**
> str get_debug_vpp_scion_ipfix_table()

Status page reporting the SCION router IPFIX table.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION router IPFIX table.
        api_response = api_instance.get_debug_vpp_scion_ipfix_table()
        print("The response of VppApi->get_debug_vpp_scion_ipfix_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_ipfix_table: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_isd_as**
> str get_debug_vpp_scion_isd_as()

Status page reporting the SCION router ASes.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION router ASes.
        api_response = api_instance.get_debug_vpp_scion_isd_as()
        print("The response of VppApi->get_debug_vpp_scion_isd_as:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_isd_as: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_reservation**
> str get_debug_vpp_scion_reservation()

Status page reporting the SCION router bandwidth reservations.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION router bandwidth reservations.
        api_response = api_instance.get_debug_vpp_scion_reservation()
        print("The response of VppApi->get_debug_vpp_scion_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_reservation: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_svc**
> str get_debug_vpp_scion_svc()

Status page reporting the SCION services.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting the SCION services.
        api_response = api_instance.get_debug_vpp_scion_svc()
        print("The response of VppApi->get_debug_vpp_scion_svc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_svc: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_decap_to_output**
> str get_debug_vpp_scion_tunneling_decap_to_output(t=t, p=p)

SCION gateway: trace all ingress IP packets.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all ingress IP packets.
        api_response = api_instance.get_debug_vpp_scion_tunneling_decap_to_output(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_decap_to_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_decap_to_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_dpdk_to_decap**
> str get_debug_vpp_scion_tunneling_dpdk_to_decap(t=t, p=p)

SCION gateway: trace all ingress frames entering via dpdk.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all ingress frames entering via dpdk.
        api_response = api_instance.get_debug_vpp_scion_tunneling_dpdk_to_decap(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_dpdk_to_decap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_dpdk_to_decap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_dpdk_to_encap4**
> str get_debug_vpp_scion_tunneling_dpdk_to_encap4(t=t, p=p)

SCION gateway: trace all egress IPv4 packets entering via dpdk.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all egress IPv4 packets entering via dpdk.
        api_response = api_instance.get_debug_vpp_scion_tunneling_dpdk_to_encap4(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_dpdk_to_encap4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_dpdk_to_encap4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_dpdk_to_encap6**
> str get_debug_vpp_scion_tunneling_dpdk_to_encap6(t=t, p=p)

SCION gateway: trace all egress IPv6 packets entering via dpdk.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all egress IPv6 packets entering via dpdk.
        api_response = api_instance.get_debug_vpp_scion_tunneling_dpdk_to_encap6(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_dpdk_to_encap6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_dpdk_to_encap6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_encap4_to_output**
> str get_debug_vpp_scion_tunneling_encap4_to_output(t=t, p=p)

SCION gateway: trace all egress frames on top of IPv4 underlay.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all egress frames on top of IPv4 underlay.
        api_response = api_instance.get_debug_vpp_scion_tunneling_encap4_to_output(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_encap4_to_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_encap4_to_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_encap6_to_output**
> str get_debug_vpp_scion_tunneling_encap6_to_output(t=t, p=p)

SCION gateway: trace all egress frames on top of IPv6 underlay.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all egress frames on top of IPv6 underlay.
        api_response = api_instance.get_debug_vpp_scion_tunneling_encap6_to_output(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_encap6_to_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_encap6_to_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_info**
> str get_debug_vpp_scion_tunneling_info()

SCION gateway: global settings.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: global settings.
        api_response = api_instance.get_debug_vpp_scion_tunneling_info()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_iremote_ia**
> str get_debug_vpp_scion_tunneling_iremote_ia()

SCION gateway: remote ASes.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: remote ASes.
        api_response = api_instance.get_debug_vpp_scion_tunneling_iremote_ia()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_iremote_ia:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_iremote_ia: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_memif_to_decap**
> str get_debug_vpp_scion_tunneling_memif_to_decap(t=t, p=p)

SCION gateway: trace all ingress frames entering via memif.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all ingress frames entering via memif.
        api_response = api_instance.get_debug_vpp_scion_tunneling_memif_to_decap(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_memif_to_decap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_memif_to_decap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_memif_to_encap4**
> str get_debug_vpp_scion_tunneling_memif_to_encap4(t=t, p=p)

SCION gateway: trace all egress IPv4 packets entering via memif.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all egress IPv4 packets entering via memif.
        api_response = api_instance.get_debug_vpp_scion_tunneling_memif_to_encap4(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_memif_to_encap4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_memif_to_encap4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_memif_to_encap6**
> str get_debug_vpp_scion_tunneling_memif_to_encap6(t=t, p=p)

SCION gateway: trace all egress IPv6 packets entering via memif.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # SCION gateway: trace all egress IPv6 packets entering via memif.
        api_response = api_instance.get_debug_vpp_scion_tunneling_memif_to_encap6(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_scion_tunneling_memif_to_encap6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_memif_to_encap6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_path**
> str get_debug_vpp_scion_tunneling_path()

SCION gateway: known paths.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: known paths.
        api_response = api_instance.get_debug_vpp_scion_tunneling_path()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_path: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_routing**
> str get_debug_vpp_scion_tunneling_routing()

SCION gateway: routing hierarchy.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: routing hierarchy.
        api_response = api_instance.get_debug_vpp_scion_tunneling_routing()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_routing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_routing_chain**
> str get_debug_vpp_scion_tunneling_routing_chain()

SCION gateway: routing chains.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: routing chains.
        api_response = api_instance.get_debug_vpp_scion_tunneling_routing_chain()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_routing_chain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_routing_chain: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_session**
> str get_debug_vpp_scion_tunneling_session()

SCION gateway: sessions.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: sessions.
        api_response = api_instance.get_debug_vpp_scion_tunneling_session()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_traffic_class**
> str get_debug_vpp_scion_tunneling_traffic_class()

SCION gateway: traffic classes.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: traffic classes.
        api_response = api_instance.get_debug_vpp_scion_tunneling_traffic_class()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_traffic_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_traffic_class: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_scion_tunneling_tun**
> str get_debug_vpp_scion_tunneling_tun()

SCION gateway: TUN device.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # SCION gateway: TUN device.
        api_response = api_instance.get_debug_vpp_scion_tunneling_tun()
        print("The response of VppApi->get_debug_vpp_scion_tunneling_tun:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_scion_tunneling_tun: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace**
> str get_debug_vpp_trace(n=n, i=i, e=e, t=t, p=p)

Action path to execute free form packet trace.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    n = '' # str | VPP node to trace. (optional) (default to '')
    i = '' # str | Include only packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    e = '' # str | Exclude packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute free form packet trace.
        api_response = api_instance.get_debug_vpp_trace(n=n, i=i, e=e, t=t, p=p)
        print("The response of VppApi->get_debug_vpp_trace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| VPP node to trace. | [optional] [default to &#39;&#39;]
 **i** | **str**| Include only packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. | [optional] [default to &#39;&#39;]
 **e** | **str**| Exclude packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. | [optional] [default to &#39;&#39;]
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_dpdk**
> str get_debug_vpp_trace_dpdk(t=t, p=p)

Action path to execute a trace for packets entering via DPDK.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for packets entering via DPDK.
        api_response = api_instance.get_debug_vpp_trace_dpdk(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_trace_dpdk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_dpdk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_memif**
> str get_debug_vpp_trace_memif(t=t, p=p)

Action path to execute a trace for packets entering via memif.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for packets entering via memif.
        api_response = api_instance.get_debug_vpp_trace_memif(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_trace_memif:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_memif: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_start**
> str get_debug_vpp_trace_start(n=n, i=i, e=e, p=p)

Action path that starts a trace without timeout. The trace can be stopped with the `/vpp/trace/stop` endpoint.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    n = '' # str | VPP node to trace. (optional) (default to '')
    i = '' # str | Include only packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    e = '' # str | Exclude packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path that starts a trace without timeout. The trace can be stopped with the `/vpp/trace/stop` endpoint.
        api_response = api_instance.get_debug_vpp_trace_start(n=n, i=i, e=e, p=p)
        print("The response of VppApi->get_debug_vpp_trace_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **str**| VPP node to trace. | [optional] [default to &#39;&#39;]
 **i** | **str**| Include only packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. | [optional] [default to &#39;&#39;]
 **e** | **str**| Exclude packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. | [optional] [default to &#39;&#39;]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_stop**
> str get_debug_vpp_trace_stop(p=p)

Action path that stops tracing.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path that stops tracing.
        api_response = api_instance.get_debug_vpp_trace_stop(p=p)
        print("The response of VppApi->get_debug_vpp_trace_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_udp4_socket**
> str get_debug_vpp_trace_udp4_socket(t=t, p=p)

Action path to execute a trace for IPv4 packets entering via VPP UDP socket.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for IPv4 packets entering via VPP UDP socket.
        api_response = api_instance.get_debug_vpp_trace_udp4_socket(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_trace_udp4_socket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_udp4_socket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_udp6_socket**
> str get_debug_vpp_trace_udp6_socket(t=t, p=p)

Action path to execute a trace for IPv6 packets entering via VPP UDP socket.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for IPv6 packets entering via VPP UDP socket.
        api_response = api_instance.get_debug_vpp_trace_udp6_socket(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_trace_udp6_socket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_udp6_socket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_trace_virtio**
> str get_debug_vpp_trace_virtio(t=t, p=p)

Action path to execute a trace for packets entering via TUN/TAP.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for packets entering via TUN/TAP.
        api_response = api_instance.get_debug_vpp_trace_virtio(t=t, p=p)
        print("The response of VppApi->get_debug_vpp_trace_virtio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_trace_virtio: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **t** | **int**| Timeout (in ms) for the trace to be stopped. | [optional] [default to 500]
 **p** | **int**| maximum number of packets to return. | [optional] [default to 50]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_tun**
> str get_debug_vpp_tun()

Status page reporting TUN/TAP devices created by VPP.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting TUN/TAP devices created by VPP.
        api_response = api_instance.get_debug_vpp_tun()
        print("The response of VppApi->get_debug_vpp_tun:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_tun: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_vpp_vrrp**
> str get_debug_vpp_vrrp()

Status page reporting VPP VRRP.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ansible.module_utils.appliance_api_client.Configuration(
    host = "https://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with ansible.module_utils.appliance_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ansible.module_utils.appliance_api_client.VppApi(api_client)

    try:
        # Status page reporting VPP VRRP.
        api_response = api_instance.get_debug_vpp_vrrp()
        print("The response of VppApi->get_debug_vpp_vrrp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppApi->get_debug_vpp_vrrp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuspage invocation response. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

