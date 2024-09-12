# openapi_client.NetworkApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_physical_interfaces_get**](NetworkApi.md#network_physical_interfaces_get) | **GET** /network/physical-interfaces | List the available physical interfaces
[**network_wireguards_get**](NetworkApi.md#network_wireguards_get) | **GET** /network/wireguards | Get list of Wireguard interfaces.
[**network_wireguards_interface_get**](NetworkApi.md#network_wireguards_interface_get) | **GET** /network/wireguards/{interface_name} | Get a Wireguard interface.


# **network_physical_interfaces_get**
> NetworkPhysicalInterfacesGetResponseJson network_physical_interfaces_get()

List the available physical interfaces

List the available physical interfaces of the appliance. The result includes the interface name and the PCI-E Bus/Device/Function (BDF) address for each interface. Only physical interfaces are listed here. To configure them use the config endpoint of the API. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_physical_interfaces_get_response_json import NetworkPhysicalInterfacesGetResponseJson
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NetworkApi(api_client)

    try:
        # List the available physical interfaces
        api_response = api_instance.network_physical_interfaces_get()
        print("The response of NetworkApi->network_physical_interfaces_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->network_physical_interfaces_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NetworkPhysicalInterfacesGetResponseJson**](NetworkPhysicalInterfacesGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_wireguards_get**
> NetworkWireguardsGetResponseJson network_wireguards_get()

Get list of Wireguard interfaces.

List the configured wireguard interfaces. The result includes the interface name and the public key. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_wireguards_get_response_json import NetworkWireguardsGetResponseJson
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NetworkApi(api_client)

    try:
        # Get list of Wireguard interfaces.
        api_response = api_instance.network_wireguards_get()
        print("The response of NetworkApi->network_wireguards_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->network_wireguards_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NetworkWireguardsGetResponseJson**](NetworkWireguardsGetResponseJson.md)

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

# **network_wireguards_interface_get**
> NetworkWireguardsInterfaceGetResponseJson network_wireguards_interface_get(interface_name)

Get a Wireguard interface.

Returns the configured wireguard interface and the public key. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.network_wireguards_interface_get_response_json import NetworkWireguardsInterfaceGetResponseJson
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:443/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:443/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NetworkApi(api_client)
    interface_name = 'interface_name_example' # str | Name of the interface to list.

    try:
        # Get a Wireguard interface.
        api_response = api_instance.network_wireguards_interface_get(interface_name)
        print("The response of NetworkApi->network_wireguards_interface_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkApi->network_wireguards_interface_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface_name** | **str**| Name of the interface to list. | 

### Return type

[**NetworkWireguardsInterfaceGetResponseJson**](NetworkWireguardsInterfaceGetResponseJson.md)

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

