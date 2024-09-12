# openapi_client.ConfigApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_get**](ConfigApi.md#config_get) | **GET** /config | Get the current configuration
[**config_put**](ConfigApi.md#config_put) | **PUT** /config | Put a new configuration
[**config_validate_post**](ConfigApi.md#config_validate_post) | **POST** /config/validate | Validates a configuration


# **config_get**
> ConfigGetResponseJson config_get(if_none_match=if_none_match, suppress_secrets=suppress_secrets)

Get the current configuration

Get the currently active appliance configuration.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.config_get_response_json import ConfigGetResponseJson
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
    api_instance = openapi_client.ConfigApi(api_client)
    if_none_match = 'if_none_match_example' # str |  (optional)
    suppress_secrets = True # bool | Do not expose secrets in the response. (optional)

    try:
        # Get the current configuration
        api_response = api_instance.config_get(if_none_match=if_none_match, suppress_secrets=suppress_secrets)
        print("The response of ConfigApi->config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_none_match** | **str**|  | [optional] 
 **suppress_secrets** | **bool**| Do not expose secrets in the response. | [optional] 

### Return type

[**ConfigGetResponseJson**](ConfigGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**304** | not modified |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_put**
> ConfigPutResponseJson config_put(config_put_request, if_match=if_match, force=force, disable_strict_parsing=disable_strict_parsing)

Put a new configuration

Put a new configuration to the appliance.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.config_put_request import ConfigPutRequest
from openapi_client.models.config_put_response_json import ConfigPutResponseJson
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
    api_instance = openapi_client.ConfigApi(api_client)
    config_put_request = openapi_client.ConfigPutRequest() # ConfigPutRequest | The config to be pushed to the appliance.
    if_match = 'if_match_example' # str |  (optional)
    force = True # bool | Push the configuration, even if configuration validation fails. This parameter MUST be used with care as it can leave the appliance in a misconfigured state. (optional)
    disable_strict_parsing = True # bool | Disable strict parsing of the appliance configuration. (optional)

    try:
        # Put a new configuration
        api_response = api_instance.config_put(config_put_request, if_match=if_match, force=force, disable_strict_parsing=disable_strict_parsing)
        print("The response of ConfigApi->config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->config_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_put_request** | [**ConfigPutRequest**](ConfigPutRequest.md)| The config to be pushed to the appliance. | 
 **if_match** | **str**|  | [optional] 
 **force** | **bool**| Push the configuration, even if configuration validation fails. This parameter MUST be used with care as it can leave the appliance in a misconfigured state. | [optional] 
 **disable_strict_parsing** | **bool**| Disable strict parsing of the appliance configuration. | [optional] 

### Return type

[**ConfigPutResponseJson**](ConfigPutResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | invalid configuration |  -  |
**412** | precondition failed |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_validate_post**
> ConfigPostResponseJson config_validate_post(config_put_request, disable_strict_parsing=disable_strict_parsing)

Validates a configuration

Validates a configuration.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.config_post_response_json import ConfigPostResponseJson
from openapi_client.models.config_put_request import ConfigPutRequest
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
    api_instance = openapi_client.ConfigApi(api_client)
    config_put_request = openapi_client.ConfigPutRequest() # ConfigPutRequest | The config to be validated.
    disable_strict_parsing = True # bool | Disable strict parsing of the appliance configuration. (optional)

    try:
        # Validates a configuration
        api_response = api_instance.config_validate_post(config_put_request, disable_strict_parsing=disable_strict_parsing)
        print("The response of ConfigApi->config_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->config_validate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_put_request** | [**ConfigPutRequest**](ConfigPutRequest.md)| The config to be validated. | 
 **disable_strict_parsing** | **bool**| Disable strict parsing of the appliance configuration. | [optional] 

### Return type

[**ConfigPostResponseJson**](ConfigPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | invalid configuration |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

