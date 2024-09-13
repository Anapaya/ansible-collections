# ansible.module_utils.appliance_api_client.VppTraceApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_debug_vpp_trace**](VppTraceApi.md#get_debug_vpp_trace) | **GET** /debug/vpp/trace | Action path to execute free form packet trace.
[**get_debug_vpp_trace_dpdk**](VppTraceApi.md#get_debug_vpp_trace_dpdk) | **GET** /debug/vpp/trace/dpdk | Action path to execute a trace for packets entering via DPDK.
[**get_debug_vpp_trace_memif**](VppTraceApi.md#get_debug_vpp_trace_memif) | **GET** /debug/vpp/trace/memif | Action path to execute a trace for packets entering via memif.
[**get_debug_vpp_trace_start**](VppTraceApi.md#get_debug_vpp_trace_start) | **GET** /debug/vpp/trace/start | Action path that starts a trace without timeout. The trace can be stopped with the &#x60;/vpp/trace/stop&#x60; endpoint.
[**get_debug_vpp_trace_stop**](VppTraceApi.md#get_debug_vpp_trace_stop) | **GET** /debug/vpp/trace/stop | Action path that stops tracing.
[**get_debug_vpp_trace_udp4_socket**](VppTraceApi.md#get_debug_vpp_trace_udp4_socket) | **GET** /debug/vpp/trace/udp4-socket | Action path to execute a trace for IPv4 packets entering via VPP UDP socket.
[**get_debug_vpp_trace_udp6_socket**](VppTraceApi.md#get_debug_vpp_trace_udp6_socket) | **GET** /debug/vpp/trace/udp6-socket | Action path to execute a trace for IPv6 packets entering via VPP UDP socket.
[**get_debug_vpp_trace_virtio**](VppTraceApi.md#get_debug_vpp_trace_virtio) | **GET** /debug/vpp/trace/virtio | Action path to execute a trace for packets entering via TUN/TAP.


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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    n = '' # str | VPP node to trace. (optional) (default to '')
    i = '' # str | Include only packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    e = '' # str | Exclude packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute free form packet trace.
        api_response = api_instance.get_debug_vpp_trace(n=n, i=i, e=e, t=t, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for packets entering via DPDK.
        api_response = api_instance.get_debug_vpp_trace_dpdk(t=t, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_dpdk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_dpdk: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for packets entering via memif.
        api_response = api_instance.get_debug_vpp_trace_memif(t=t, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_memif:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_memif: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    n = '' # str | VPP node to trace. (optional) (default to '')
    i = '' # str | Include only packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    e = '' # str | Exclude packets passing through the specified VPP node. Include and exclude parameters are mutually exclusive. (optional) (default to '')
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path that starts a trace without timeout. The trace can be stopped with the `/vpp/trace/stop` endpoint.
        api_response = api_instance.get_debug_vpp_trace_start(n=n, i=i, e=e, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_start: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path that stops tracing.
        api_response = api_instance.get_debug_vpp_trace_stop(p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_stop: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for IPv4 packets entering via VPP UDP socket.
        api_response = api_instance.get_debug_vpp_trace_udp4_socket(t=t, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_udp4_socket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_udp4_socket: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for IPv6 packets entering via VPP UDP socket.
        api_response = api_instance.get_debug_vpp_trace_udp6_socket(t=t, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_udp6_socket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_udp6_socket: %s\n" % e)
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
    api_instance = ansible.module_utils.appliance_api_client.VppTraceApi(api_client)
    t = 500 # int | Timeout (in ms) for the trace to be stopped. (optional) (default to 500)
    p = 50 # int | maximum number of packets to return. (optional) (default to 50)

    try:
        # Action path to execute a trace for packets entering via TUN/TAP.
        api_response = api_instance.get_debug_vpp_trace_virtio(t=t, p=p)
        print("The response of VppTraceApi->get_debug_vpp_trace_virtio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VppTraceApi->get_debug_vpp_trace_virtio: %s\n" % e)
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

