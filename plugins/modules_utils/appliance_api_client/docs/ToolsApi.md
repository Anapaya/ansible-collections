# openapi_client.ToolsApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tools_scion_ping_post**](ToolsApi.md#tools_scion_ping_post) | **POST** /tools/scion/ping | Trigger a scion ping run
[**tools_scion_showpaths_post**](ToolsApi.md#tools_scion_showpaths_post) | **POST** /tools/scion/showpaths | Trigger a SCION showpaths request
[**tools_scion_traceroute_post**](ToolsApi.md#tools_scion_traceroute_post) | **POST** /tools/scion/traceroute | Trigger a scion traceroute run


# **tools_scion_ping_post**
> ToolsScionPingPostResponseJson tools_scion_ping_post(tools_scion_ping_post_request=tools_scion_ping_post_request)

Trigger a scion ping run

Trigger and wait for a ping run to test connectivity to a remote SCION host using SCMP echo packets. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.tools_scion_ping_post_request import ToolsScionPingPostRequest
from openapi_client.models.tools_scion_ping_post_response_json import ToolsScionPingPostResponseJson
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
    api_instance = openapi_client.ToolsApi(api_client)
    tools_scion_ping_post_request = openapi_client.ToolsScionPingPostRequest() # ToolsScionPingPostRequest |  (optional)

    try:
        # Trigger a scion ping run
        api_response = api_instance.tools_scion_ping_post(tools_scion_ping_post_request=tools_scion_ping_post_request)
        print("The response of ToolsApi->tools_scion_ping_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->tools_scion_ping_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tools_scion_ping_post_request** | [**ToolsScionPingPostRequest**](ToolsScionPingPostRequest.md)|  | [optional] 

### Return type

[**ToolsScionPingPostResponseJson**](ToolsScionPingPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tools_scion_showpaths_post**
> ToolsScionShowpathsPostResponseJson tools_scion_showpaths_post(tools_scion_showpaths_post_request=tools_scion_showpaths_post_request)

Trigger a SCION showpaths request

Trigger a SCION showpaths request to a remote SCION AS. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.tools_scion_showpaths_post_request import ToolsScionShowpathsPostRequest
from openapi_client.models.tools_scion_showpaths_post_response_json import ToolsScionShowpathsPostResponseJson
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
    api_instance = openapi_client.ToolsApi(api_client)
    tools_scion_showpaths_post_request = openapi_client.ToolsScionShowpathsPostRequest() # ToolsScionShowpathsPostRequest |  (optional)

    try:
        # Trigger a SCION showpaths request
        api_response = api_instance.tools_scion_showpaths_post(tools_scion_showpaths_post_request=tools_scion_showpaths_post_request)
        print("The response of ToolsApi->tools_scion_showpaths_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->tools_scion_showpaths_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tools_scion_showpaths_post_request** | [**ToolsScionShowpathsPostRequest**](ToolsScionShowpathsPostRequest.md)|  | [optional] 

### Return type

[**ToolsScionShowpathsPostResponseJson**](ToolsScionShowpathsPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tools_scion_traceroute_post**
> ToolsScionTraceroutePostResponseJson tools_scion_traceroute_post(tools_scion_traceroute_post_request=tools_scion_traceroute_post_request)

Trigger a scion traceroute run

Trigger a SCION traceroute run and trace the SCION path to a remote AS using SCMP traceroute packets. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.tools_scion_traceroute_post_request import ToolsScionTraceroutePostRequest
from openapi_client.models.tools_scion_traceroute_post_response_json import ToolsScionTraceroutePostResponseJson
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
    api_instance = openapi_client.ToolsApi(api_client)
    tools_scion_traceroute_post_request = openapi_client.ToolsScionTraceroutePostRequest() # ToolsScionTraceroutePostRequest |  (optional)

    try:
        # Trigger a scion traceroute run
        api_response = api_instance.tools_scion_traceroute_post(tools_scion_traceroute_post_request=tools_scion_traceroute_post_request)
        print("The response of ToolsApi->tools_scion_traceroute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->tools_scion_traceroute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tools_scion_traceroute_post_request** | [**ToolsScionTraceroutePostRequest**](ToolsScionTraceroutePostRequest.md)|  | [optional] 

### Return type

[**ToolsScionTraceroutePostResponseJson**](ToolsScionTraceroutePostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

