# openapi_client.HealthApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_get**](HealthApi.md#health_get) | **GET** /health | Appliance Health


# **health_get**
> HealthGetResponseJson health_get(check_id=check_id, service_name=service_name, status=status)

Appliance Health

Report the appliance health along with the executed health checks. The health status is based on a set of health checks that are executed. Check the documentation of the individual health checks for more information.  Note that the status is only based on the health checks that are part of the response. If you filter out non-passing health checks, the top level status will be reported as passing. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.health_get_response_json import HealthGetResponseJson
from openapi_client.models.health_status import HealthStatus
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
    api_instance = openapi_client.HealthApi(api_client)
    check_id = ['check_id_example'] # List[str] | List of check_id (or check_id prefixes) that should be included in the response. If unset, health checks are not filtered by check_id.  (optional)
    service_name = ['service_name_example'] # List[str] | List of service_name (or service_name prefixes) that should be included in the response. If unset, health checks are not filtered by service_name.  (optional)
    status = [openapi_client.HealthStatus()] # List[HealthStatus] | List of status that should be included in the response. If unset, health checks are not filtered by status.  (optional)

    try:
        # Appliance Health
        api_response = api_instance.health_get(check_id=check_id, service_name=service_name, status=status)
        print("The response of HealthApi->health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->health_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_id** | [**List[str]**](str.md)| List of check_id (or check_id prefixes) that should be included in the response. If unset, health checks are not filtered by check_id.  | [optional] 
 **service_name** | [**List[str]**](str.md)| List of service_name (or service_name prefixes) that should be included in the response. If unset, health checks are not filtered by service_name.  | [optional] 
 **status** | [**List[HealthStatus]**](HealthStatus.md)| List of status that should be included in the response. If unset, health checks are not filtered by status.  | [optional] 

### Return type

[**HealthGetResponseJson**](HealthGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

