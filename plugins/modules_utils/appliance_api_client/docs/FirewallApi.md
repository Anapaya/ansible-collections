# openapi_client.FirewallApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewall_chain_get**](FirewallApi.md#firewall_chain_get) | **GET** /firewall/tables/{table_name}/chains/{chain_name} | Get the rules of a chain of a firewall table.
[**firewall_default_post**](FirewallApi.md#firewall_default_post) | **POST** /firewall/default | Generate the default firewall configuration for the given appliance configuration.
[**firewall_get**](FirewallApi.md#firewall_get) | **GET** /firewall | Get the firewall configuration of the appliance.
[**firewall_table_get**](FirewallApi.md#firewall_table_get) | **GET** /firewall/tables/{table_name} | Get a specific firewall table.


# **firewall_chain_get**
> FirewallChainJson firewall_chain_get(table_name, chain_name)

Get the rules of a chain of a firewall table.

Get a specific set of rules specified by their chain and table name of the appliance firewall. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_chain_json import FirewallChainJson
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
    api_instance = openapi_client.FirewallApi(api_client)
    table_name = 'table_name_example' # str | 
    chain_name = 'chain_name_example' # str | 

    try:
        # Get the rules of a chain of a firewall table.
        api_response = api_instance.firewall_chain_get(table_name, chain_name)
        print("The response of FirewallApi->firewall_chain_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->firewall_chain_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**|  | 
 **chain_name** | **str**|  | 

### Return type

[**FirewallChainJson**](FirewallChainJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firewall chain. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firewall_default_post**
> FirewallsJson firewall_default_post(config_put_request, disable_strict_parsing=disable_strict_parsing)

Generate the default firewall configuration for the given appliance configuration.

Validates a configuration and returns the firewall configuration which would be applied for the given appliance configuration.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.config_put_request import ConfigPutRequest
from openapi_client.models.firewalls_json import FirewallsJson
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
    api_instance = openapi_client.FirewallApi(api_client)
    config_put_request = openapi_client.ConfigPutRequest() # ConfigPutRequest | The config to be validated.
    disable_strict_parsing = True # bool | Disable strict parsing of the appliance configuration. (optional)

    try:
        # Generate the default firewall configuration for the given appliance configuration.
        api_response = api_instance.firewall_default_post(config_put_request, disable_strict_parsing=disable_strict_parsing)
        print("The response of FirewallApi->firewall_default_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->firewall_default_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_put_request** | [**ConfigPutRequest**](ConfigPutRequest.md)| The config to be validated. | 
 **disable_strict_parsing** | **bool**| Disable strict parsing of the appliance configuration. | [optional] 

### Return type

[**FirewallsJson**](FirewallsJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firewall configuration. |  -  |
**400** | invalid configuration |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firewall_get**
> FirewallsJson firewall_get()

Get the firewall configuration of the appliance.

Get the installed firewall configuration of the appliance, including the tables, named counters, chains and rules. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewalls_json import FirewallsJson
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
    api_instance = openapi_client.FirewallApi(api_client)

    try:
        # Get the firewall configuration of the appliance.
        api_response = api_instance.firewall_get()
        print("The response of FirewallApi->firewall_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->firewall_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FirewallsJson**](FirewallsJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firewall configuration. |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firewall_table_get**
> FirewallTableJson firewall_table_get(table_name)

Get a specific firewall table.

Get a specific firewall table of the appliance by name, including the named counters, chains, and their rules. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.firewall_table_json import FirewallTableJson
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
    api_instance = openapi_client.FirewallApi(api_client)
    table_name = 'table_name_example' # str | 

    try:
        # Get a specific firewall table.
        api_response = api_instance.firewall_table_get(table_name)
        print("The response of FirewallApi->firewall_table_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->firewall_table_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_name** | **str**|  | 

### Return type

[**FirewallTableJson**](FirewallTableJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firewall table. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

