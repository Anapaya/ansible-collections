# ansible.module_utils.appliance_api_client.DebugApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debug_bgp_config_get**](DebugApi.md#debug_bgp_config_get) | **GET** /debug/bgp/config | Get the BGP configuration.
[**debug_bgp_neighbors_get**](DebugApi.md#debug_bgp_neighbors_get) | **GET** /debug/bgp/neighbors | Get the state of the BGP neighbors.
[**debug_cluster_status_get**](DebugApi.md#debug_cluster_status_get) | **GET** /debug/cluster/status | Get the cluster status.
[**debug_lan_monitoring_get**](DebugApi.md#debug_lan_monitoring_get) | **GET** /debug/lan-monitoring | Get LAN statistics.
[**debug_logs_entries_get**](DebugApi.md#debug_logs_entries_get) | **GET** /debug/logs/entries | Retrieve logs via systemd-journal-gatewayd compatible interface.
[**debug_network_interfaces_get**](DebugApi.md#debug_network_interfaces_get) | **GET** /debug/network/interfaces | Network interfaces summary.
[**debug_network_planner_graph_get**](DebugApi.md#debug_network_planner_graph_get) | **GET** /debug/network/planner/graph | The graph of planner nodes.
[**debug_network_routes_get**](DebugApi.md#debug_network_routes_get) | **GET** /debug/network/routes | Network routes summary.
[**debug_notifications_get**](DebugApi.md#debug_notifications_get) | **GET** /debug/notifications | Get if the periodic appliance-controller notifications are enabled.
[**debug_notifications_post**](DebugApi.md#debug_notifications_post) | **POST** /debug/notifications | Trigger a notification from the appliance-controller.
[**debug_notifications_put**](DebugApi.md#debug_notifications_put) | **PUT** /debug/notifications | Enable or disable periodic notifications from the appliance-controller.
[**debug_scion_interfaces_get**](DebugApi.md#debug_scion_interfaces_get) | **GET** /debug/scion/interfaces | Get the SCION interfaces.
[**debug_scion_tunneling_discovery_get**](DebugApi.md#debug_scion_tunneling_discovery_get) | **GET** /debug/scion-tunneling/discovery | Discovery of tunneling peers.
[**debug_scion_tunneling_domains_config_get**](DebugApi.md#debug_scion_tunneling_domains_config_get) | **GET** /debug/scion-tunneling/domains/config | Get the SCION tunneling domains configuration.
[**debug_scion_tunneling_paths_get**](DebugApi.md#debug_scion_tunneling_paths_get) | **GET** /debug/scion-tunneling/paths | List of all SCION paths with their stats.
[**debug_scion_tunneling_paths_search_post**](DebugApi.md#debug_scion_tunneling_paths_search_post) | **POST** /debug/scion-tunneling/paths/search | List of SCION paths with their stats.
[**debug_scion_tunneling_planner_graph_get**](DebugApi.md#debug_scion_tunneling_planner_graph_get) | **GET** /debug/scion-tunneling/planner/graph | The graph of the planner nodes and dependencies.
[**debug_scion_tunneling_sa_reset_post**](DebugApi.md#debug_scion_tunneling_sa_reset_post) | **POST** /debug/scion-tunneling/sa/reset | Reset the SAs of the SCION tunnels.
[**debug_scion_tunneling_sgrp_domains_get**](DebugApi.md#debug_scion_tunneling_sgrp_domains_get) | **GET** /debug/scion-tunneling/sgrp/domains | SGRP domains.
[**debug_scion_tunneling_sgrp_local_prefixes_get**](DebugApi.md#debug_scion_tunneling_sgrp_local_prefixes_get) | **GET** /debug/scion-tunneling/sgrp/local-prefixes | Known local network prefixes.
[**debug_scion_tunneling_sgrp_peers_get**](DebugApi.md#debug_scion_tunneling_sgrp_peers_get) | **GET** /debug/scion-tunneling/sgrp/peers | SGRP peers.
[**debug_scion_tunneling_state_current_get**](DebugApi.md#debug_scion_tunneling_state_current_get) | **GET** /debug/scion-tunneling/state/current | The full current state of the gateway.
[**debug_scion_tunneling_state_domains_get**](DebugApi.md#debug_scion_tunneling_state_domains_get) | **GET** /debug/scion-tunneling/state/domains | The user-provided domain configuration.
[**debug_scion_tunneling_state_monitored_get**](DebugApi.md#debug_scion_tunneling_state_monitored_get) | **GET** /debug/scion-tunneling/state/monitored | The state monitored by the gateway.
[**debug_scion_tunneling_state_observability_get**](DebugApi.md#debug_scion_tunneling_state_observability_get) | **GET** /debug/scion-tunneling/state/observability | The full dump of observability data.
[**debug_scion_tunneling_summary_get**](DebugApi.md#debug_scion_tunneling_summary_get) | **GET** /debug/scion-tunneling/summary | Get summary of the SCION tunneling infrastructure.
[**debug_service_groups_restart_post**](DebugApi.md#debug_service_groups_restart_post) | **POST** /debug/service-groups/{group_name}/restart | Restart group of services.
[**debug_services_get**](DebugApi.md#debug_services_get) | **GET** /debug/services | Get the list of appliance services and service groups.
[**debug_services_health**](DebugApi.md#debug_services_health) | **GET** /debug/services/{service_name}/health | Indicate the service health.
[**debug_services_health_summary**](DebugApi.md#debug_services_health_summary) | **GET** /debug/service-health | Summary of all service health checks.
[**debug_services_restart**](DebugApi.md#debug_services_restart) | **POST** /debug/services/{service_name}/restart | Restarts the given service.


# **debug_bgp_config_get**
> BGPResponseJson debug_bgp_config_get()

Get the BGP configuration.

Get the BGP configuration of the host.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.bgp_response_json import BGPResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get the BGP configuration.
        api_response = api_instance.debug_bgp_config_get()
        print("The response of DebugApi->debug_bgp_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_bgp_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BGPResponseJson**](BGPResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BGP configuration. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_bgp_neighbors_get**
> BGPNeighborsResponseJson debug_bgp_neighbors_get()

Get the state of the BGP neighbors.

Get the state of the BGP neighbors.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.bgp_neighbors_response_json import BGPNeighborsResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get the state of the BGP neighbors.
        api_response = api_instance.debug_bgp_neighbors_get()
        print("The response of DebugApi->debug_bgp_neighbors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_bgp_neighbors_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BGPNeighborsResponseJson**](BGPNeighborsResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BGP neighbor state. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_cluster_status_get**
> DebugClusterStatus debug_cluster_status_get()

Get the cluster status.

Get the status of the cluster. The status includes for each peer the name, the address, the time of the last synchronization, the status of said synchronization, and if the attempt failed the reason for the failure. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.debug_cluster_status import DebugClusterStatus
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get the cluster status.
        api_response = api_instance.debug_cluster_status_get()
        print("The response of DebugApi->debug_cluster_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_cluster_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DebugClusterStatus**](DebugClusterStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cluster status. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_lan_monitoring_get**
> LanStats debug_lan_monitoring_get()

Get LAN statistics.

Get LAN statistics. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.lan_stats import LanStats
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get LAN statistics.
        api_response = api_instance.debug_lan_monitoring_get()
        print("The response of DebugApi->debug_lan_monitoring_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_lan_monitoring_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LanStats**](LanStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LAN statistics |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_logs_entries_get**
> debug_logs_entries_get(range=range, accept=accept)

Retrieve logs via systemd-journal-gatewayd compatible interface.

Endpoint that implemenets the interface exposed via the /entries endpoint of the systemd-journal-gatewayd service. By default, all systemd-journal logs are exposed.  See also: https://www.freedesktop.org/software/systemd/man/latest/systemd-journal-gatewayd.service.html 

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    range = 'range_example' # str | The range of requested log entries. See systemd-journal-gatewayd documentation. (optional)
    accept = 'accept_example' # str | The format of the log entries (default is text). (optional)

    try:
        # Retrieve logs via systemd-journal-gatewayd compatible interface.
        api_instance.debug_logs_entries_get(range=range, accept=accept)
    except Exception as e:
        print("Exception when calling DebugApi->debug_logs_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **range** | **str**| The range of requested log entries. See systemd-journal-gatewayd documentation. | [optional] 
 **accept** | **str**| The format of the log entries (default is text). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Journald entries |  -  |
**400** | Malformed request parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_network_interfaces_get**
> NetworkInterfaces debug_network_interfaces_get(interface_name=interface_name)

Network interfaces summary.

Network interfaces summary.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.network_interfaces import NetworkInterfaces
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    interface_name = 'interface_name_example' # str |  (optional)

    try:
        # Network interfaces summary.
        api_response = api_instance.debug_network_interfaces_get(interface_name=interface_name)
        print("The response of DebugApi->debug_network_interfaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_network_interfaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_name** | **str**|  | [optional] 

### Return type

[**NetworkInterfaces**](NetworkInterfaces.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network interfaces. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_network_planner_graph_get**
> str debug_network_planner_graph_get()

The graph of planner nodes.

The graph of planner nodes. The graph is in dot format and can be rendered by graphviz, or one of the online dot-rendering tools. 

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # The graph of planner nodes.
        api_response = api_instance.debug_network_planner_graph_get()
        print("The response of DebugApi->debug_network_planner_graph_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_network_planner_graph_get: %s\n" % e)
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
**200** | The planner graph. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_network_routes_get**
> NetworkRoutes debug_network_routes_get(ip=ip)

Network routes summary.

Network routes summary.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.network_routes import NetworkRoutes
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    ip = 'ip_example' # str |  (optional)

    try:
        # Network routes summary.
        api_response = api_instance.debug_network_routes_get(ip=ip)
        print("The response of DebugApi->debug_network_routes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_network_routes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**|  | [optional] 

### Return type

[**NetworkRoutes**](NetworkRoutes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network routes. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_notifications_get**
> DebugNotifyStatusJson debug_notifications_get()

Get if the periodic appliance-controller notifications are enabled.

Check if the controller notifications are enabled or not. For context: If notifications are enabled, the appliance-controller periodically sends notifications with the latest configuration, which eventually overwrites any manual changes. By default, the controller notifications should be enabled. However, in the case of manual troubleshooting, it may be convenient to temporarily disable the controller notifications. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.debug_notify_status_json import DebugNotifyStatusJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get if the periodic appliance-controller notifications are enabled.
        api_response = api_instance.debug_notifications_get()
        print("The response of DebugApi->debug_notifications_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_notifications_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DebugNotifyStatusJson**](DebugNotifyStatusJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the status of appliance-controller notifications |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_notifications_post**
> debug_notifications_post()

Trigger a notification from the appliance-controller.

Triggering a notification will reapply the lastest stored configuration. 

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Trigger a notification from the appliance-controller.
        api_instance.debug_notifications_post()
    except Exception as e:
        print("Exception when calling DebugApi->debug_notifications_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The notification was triggered |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_notifications_put**
> DebugNotifyStatusJson debug_notifications_put(debug_notify_status_json)

Enable or disable periodic notifications from the appliance-controller.

Enable or disable the appliance-controller notifications. Optionally, a deadline can be provided, either as absolute time or as a relative duration. The deadline indicates until when the appliance-controller notifications should be disabled. If both absolute and relative times are given, the minimum is taken. For context: If notifications are enabled (default), the appliance-controller periodically sends notifications with the latest configuration, which overwrites any manual changes. Note that disabling notifications should only happen when debugging the configuration of the host. It should not be treated as a permanent solution to configuration changes, meaning that eventually the appliance-controller notifications should be re-enabled. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.debug_notify_status_json import DebugNotifyStatusJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    debug_notify_status_json = ansible.module_utils.appliance_api_client.DebugNotifyStatusJson() # DebugNotifyStatusJson | 

    try:
        # Enable or disable periodic notifications from the appliance-controller.
        api_response = api_instance.debug_notifications_put(debug_notify_status_json)
        print("The response of DebugApi->debug_notifications_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_notifications_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debug_notify_status_json** | [**DebugNotifyStatusJson**](DebugNotifyStatusJson.md)|  | 

### Return type

[**DebugNotifyStatusJson**](DebugNotifyStatusJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status of appliance-controller notifications |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_interfaces_get**
> DebugScionInterfaces debug_scion_interfaces_get(local_isd_as=local_isd_as, remote_isd_as=remote_isd_as, interface_id=interface_id)

Get the SCION interfaces.

Get a list of all the SCION interfaces configured on the host. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.debug_scion_interfaces import DebugScionInterfaces
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    local_isd_as = 'local_isd_as_example' # str |  (optional)
    remote_isd_as = 'remote_isd_as_example' # str |  (optional)
    interface_id = 56 # int |  (optional)

    try:
        # Get the SCION interfaces.
        api_response = api_instance.debug_scion_interfaces_get(local_isd_as=local_isd_as, remote_isd_as=remote_isd_as, interface_id=interface_id)
        print("The response of DebugApi->debug_scion_interfaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_interfaces_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_isd_as** | **str**|  | [optional] 
 **remote_isd_as** | **str**|  | [optional] 
 **interface_id** | **int**|  | [optional] 

### Return type

[**DebugScionInterfaces**](DebugScionInterfaces.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of SCION interfaces. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_discovery_get**
> ScionTunnelingDiscovery debug_scion_tunneling_discovery_get()

Discovery of tunneling peers.

Discovery of tunneling peers.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_discovery import ScionTunnelingDiscovery
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Discovery of tunneling peers.
        api_response = api_instance.debug_scion_tunneling_discovery_get()
        print("The response of DebugApi->debug_scion_tunneling_discovery_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_discovery_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScionTunnelingDiscovery**](ScionTunnelingDiscovery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tunneling peers discovery. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_domains_config_get**
> ScionTunnelingDomainsResponseJson debug_scion_tunneling_domains_config_get(domain=domain)

Get the SCION tunneling domains configuration.

Get the SCION tunneling domains configuration. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_domains_response_json import ScionTunnelingDomainsResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    domain = 'domain_example' # str |  (optional)

    try:
        # Get the SCION tunneling domains configuration.
        api_response = api_instance.debug_scion_tunneling_domains_config_get(domain=domain)
        print("The response of DebugApi->debug_scion_tunneling_domains_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_domains_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | [optional] 

### Return type

[**ScionTunnelingDomainsResponseJson**](ScionTunnelingDomainsResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SCION tunneling domains configuration. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_paths_get**
> ScionTunnelingPathsSearchResponseJson debug_scion_tunneling_paths_get()

List of all SCION paths with their stats.

Returns a list of all SCION paths and their stats.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_paths_search_response_json import ScionTunnelingPathsSearchResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # List of all SCION paths with their stats.
        api_response = api_instance.debug_scion_tunneling_paths_get()
        print("The response of DebugApi->debug_scion_tunneling_paths_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_paths_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScionTunnelingPathsSearchResponseJson**](ScionTunnelingPathsSearchResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all SCION paths and their stats. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_paths_search_post**
> ScionTunnelingPathsSearchResponseJson debug_scion_tunneling_paths_search_post(scion_tunneling_paths_search_post_request_json=scion_tunneling_paths_search_post_request_json)

List of SCION paths with their stats.

Returns a list of all SCION paths and their stats filtered by the fingerprints provided in the request body.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_paths_search_post_request_json import ScionTunnelingPathsSearchPostRequestJson
from ansible.module_utils.appliance_api_client.models.scion_tunneling_paths_search_response_json import ScionTunnelingPathsSearchResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    scion_tunneling_paths_search_post_request_json = ansible.module_utils.appliance_api_client.ScionTunnelingPathsSearchPostRequestJson() # ScionTunnelingPathsSearchPostRequestJson |  (optional)

    try:
        # List of SCION paths with their stats.
        api_response = api_instance.debug_scion_tunneling_paths_search_post(scion_tunneling_paths_search_post_request_json=scion_tunneling_paths_search_post_request_json)
        print("The response of DebugApi->debug_scion_tunneling_paths_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_paths_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scion_tunneling_paths_search_post_request_json** | [**ScionTunnelingPathsSearchPostRequestJson**](ScionTunnelingPathsSearchPostRequestJson.md)|  | [optional] 

### Return type

[**ScionTunnelingPathsSearchResponseJson**](ScionTunnelingPathsSearchResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all SCION paths and their stats filtered by the fingerprints provided in the request body.. |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_planner_graph_get**
> str debug_scion_tunneling_planner_graph_get()

The graph of the planner nodes and dependencies.

The graph of the planner nodes and dependencies. The graph is in the dot format and can be rendered by graphviz, or one of the online dot-rendering tools. 

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # The graph of the planner nodes and dependencies.
        api_response = api_instance.debug_scion_tunneling_planner_graph_get()
        print("The response of DebugApi->debug_scion_tunneling_planner_graph_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_planner_graph_get: %s\n" % e)
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
**200** | The planner graph. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_sa_reset_post**
> debug_scion_tunneling_sa_reset_post()

Reset the SAs of the SCION tunnels.

Reset the SAs of the SCION tunnels.

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Reset the SAs of the SCION tunnels.
        api_instance.debug_scion_tunneling_sa_reset_post()
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_sa_reset_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully reset the SAs of the SCION tunnels. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_sgrp_domains_get**
> ScionTunnelingSGRPDomains debug_scion_tunneling_sgrp_domains_get(domain=domain)

SGRP domains.

SGRP domains with the associated network prefixes.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_domains import ScionTunnelingSGRPDomains
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    domain = 'domain_example' # str |  (optional)

    try:
        # SGRP domains.
        api_response = api_instance.debug_scion_tunneling_sgrp_domains_get(domain=domain)
        print("The response of DebugApi->debug_scion_tunneling_sgrp_domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_sgrp_domains_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**|  | [optional] 

### Return type

[**ScionTunnelingSGRPDomains**](ScionTunnelingSGRPDomains.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SGRP domains. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_sgrp_local_prefixes_get**
> ScionTunnelingSGRPLocalPrefixesJSON debug_scion_tunneling_sgrp_local_prefixes_get()

Known local network prefixes.

Known local network prefixes, including their source. These are afterwards filtered according to domain definitions and eventually sent to SGRP peers. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_local_prefixes_json import ScionTunnelingSGRPLocalPrefixesJSON
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Known local network prefixes.
        api_response = api_instance.debug_scion_tunneling_sgrp_local_prefixes_get()
        print("The response of DebugApi->debug_scion_tunneling_sgrp_local_prefixes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_sgrp_local_prefixes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScionTunnelingSGRPLocalPrefixesJSON**](ScionTunnelingSGRPLocalPrefixesJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Known local network prefixes. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_sgrp_peers_get**
> ScionTunnelingSGRPPeers debug_scion_tunneling_sgrp_peers_get(local_isd_as=local_isd_as, remote_isd_as=remote_isd_as)

SGRP peers.

SGRP peers. Peer is a remote SGRP-capable application accessed from a specific local ISD-AS. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_sgrp_peers import ScionTunnelingSGRPPeers
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    local_isd_as = 'local_isd_as_example' # str |  (optional)
    remote_isd_as = 'remote_isd_as_example' # str |  (optional)

    try:
        # SGRP peers.
        api_response = api_instance.debug_scion_tunneling_sgrp_peers_get(local_isd_as=local_isd_as, remote_isd_as=remote_isd_as)
        print("The response of DebugApi->debug_scion_tunneling_sgrp_peers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_sgrp_peers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_isd_as** | **str**|  | [optional] 
 **remote_isd_as** | **str**|  | [optional] 

### Return type

[**ScionTunnelingSGRPPeers**](ScionTunnelingSGRPPeers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SGRP peers. |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_state_current_get**
> object debug_scion_tunneling_state_current_get()

The full current state of the gateway.

The full current state of the gateway.

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # The full current state of the gateway.
        api_response = api_instance.debug_scion_tunneling_state_current_get()
        print("The response of DebugApi->debug_scion_tunneling_state_current_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_state_current_get: %s\n" % e)
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
**200** | The full current state of the gateway. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_state_domains_get**
> object debug_scion_tunneling_state_domains_get()

The user-provided domain configuration.

The user-provided domain configuration.

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # The user-provided domain configuration.
        api_response = api_instance.debug_scion_tunneling_state_domains_get()
        print("The response of DebugApi->debug_scion_tunneling_state_domains_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_state_domains_get: %s\n" % e)
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
**200** | The user-provided domain configuration. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_state_monitored_get**
> object debug_scion_tunneling_state_monitored_get()

The state monitored by the gateway.

The state monitored by the gateway.

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # The state monitored by the gateway.
        api_response = api_instance.debug_scion_tunneling_state_monitored_get()
        print("The response of DebugApi->debug_scion_tunneling_state_monitored_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_state_monitored_get: %s\n" % e)
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
**200** | The state monitored by the gateway. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_state_observability_get**
> object debug_scion_tunneling_state_observability_get(filter=filter)

The full dump of observability data.

The full dump of observability data.

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    filter = ['filter_example'] # List[str] | A list of subsections to return, separated by commas. If empty, all subsections are returned.  (optional)

    try:
        # The full dump of observability data.
        api_response = api_instance.debug_scion_tunneling_state_observability_get(filter=filter)
        print("The response of DebugApi->debug_scion_tunneling_state_observability_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_state_observability_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**List[str]**](str.md)| A list of subsections to return, separated by commas. If empty, all subsections are returned.  | [optional] 

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
**200** | The full dump of observability data. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_scion_tunneling_summary_get**
> ScionTunnelingSummary debug_scion_tunneling_summary_get()

Get summary of the SCION tunneling infrastructure.

Get summary of the SCION tunneling infrastructure. 

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.scion_tunneling_summary import ScionTunnelingSummary
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get summary of the SCION tunneling infrastructure.
        api_response = api_instance.debug_scion_tunneling_summary_get()
        print("The response of DebugApi->debug_scion_tunneling_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_scion_tunneling_summary_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ScionTunnelingSummary**](ScionTunnelingSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SCION tunneling infrastructure summary |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_service_groups_restart_post**
> DebugServiceGroupsRestartResponseJson debug_service_groups_restart_post(group_name)

Restart group of services.

Trigger restart of all the services in a group.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.debug_service_groups_restart_response_json import DebugServiceGroupsRestartResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    group_name = 'group_name_example' # str | Name of the service groups to restart.

    try:
        # Restart group of services.
        api_response = api_instance.debug_service_groups_restart_post(group_name)
        print("The response of DebugApi->debug_service_groups_restart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_service_groups_restart_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Name of the service groups to restart. | 

### Return type

[**DebugServiceGroupsRestartResponseJson**](DebugServiceGroupsRestartResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_services_get**
> DebugServicesResponseJson debug_services_get()

Get the list of appliance services and service groups.

Get the list of services and service groups that must be running on the appliance.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.debug_services_response_json import DebugServicesResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Get the list of appliance services and service groups.
        api_response = api_instance.debug_services_get()
        print("The response of DebugApi->debug_services_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_services_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DebugServicesResponseJson**](DebugServicesResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of services and groups. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_services_health**
> HealthResponse debug_services_health(service_name)

Indicate the service health.

Present the health of the service along with the executed health checks.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.health_response import HealthResponse
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    service_name = 'service_name_example' # str | Name of the service to get health of.

    try:
        # Indicate the service health.
        api_response = api_instance.debug_services_health(service_name)
        print("The response of DebugApi->debug_services_health:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_services_health: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| Name of the service to get health of. | 

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service health information. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_services_health_summary**
> HealthSummaryResponse debug_services_health_summary()

Summary of all service health checks.

Present the health of all the services along with the executed health checks.

### Example


```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.health_summary_response import HealthSummaryResponse
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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)

    try:
        # Summary of all service health checks.
        api_response = api_instance.debug_services_health_summary()
        print("The response of DebugApi->debug_services_health_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_services_health_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthSummaryResponse**](HealthSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service health information. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debug_services_restart**
> object debug_services_restart(service_name)

Restarts the given service.

Restarts the given service.

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
    api_instance = ansible.module_utils.appliance_api_client.DebugApi(api_client)
    service_name = 'service_name_example' # str | Name of the service to restart.

    try:
        # Restarts the given service.
        api_response = api_instance.debug_services_restart(service_name)
        print("The response of DebugApi->debug_services_restart:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->debug_services_restart: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| Name of the service to restart. | 

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
**200** | Successful restart |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

