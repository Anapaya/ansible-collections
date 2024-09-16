# ansible.module_utils.appliance_api_client.ConfigApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_advanced_service_customization_get**](ConfigApi.md#config_advanced_service_customization_get) | **GET** /config/advanced/service-customization/{service_type} | Get the customization for a service.
[**config_advanced_service_customization_template_get**](ConfigApi.md#config_advanced_service_customization_template_get) | **GET** /config/advanced/service-customization/{service_type}/template | Get the custom template for a service.
[**config_advanced_service_customization_template_put**](ConfigApi.md#config_advanced_service_customization_template_put) | **PUT** /config/advanced/service-customization/{service_type}/template | Put a custom template for a service.
[**config_get**](ConfigApi.md#config_get) | **GET** /config | Get the current configuration
[**config_put**](ConfigApi.md#config_put) | **PUT** /config | Put a new configuration
[**config_validate_post**](ConfigApi.md#config_validate_post) | **POST** /config/validate | Validates a configuration


# **config_advanced_service_customization_get**
> ConfigServiceCustomizationResponseJson config_advanced_service_customization_get(service_type)

Get the customization for a service.

Get the configured customization for a service, along with its state.

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.config_service_customization_response_json import ConfigServiceCustomizationResponseJson
from ansible.module_utils.appliance_api_client.models.service_type import ServiceType
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
    api_instance = ansible.module_utils.appliance_api_client.ConfigApi(api_client)
    service_type = ansible.module_utils.appliance_api_client.ServiceType() # ServiceType | Service Type

    try:
        # Get the customization for a service.
        api_response = api_instance.config_advanced_service_customization_get(service_type)
        print("The response of ConfigApi->config_advanced_service_customization_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->config_advanced_service_customization_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_type** | [**ServiceType**](.md)| Service Type | 

### Return type

[**ConfigServiceCustomizationResponseJson**](ConfigServiceCustomizationResponseJson.md)

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

# **config_advanced_service_customization_template_get**
> str config_advanced_service_customization_template_get(service_type)

Get the custom template for a service.

Get the configured custom template for a service, along with its state.

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.service_type import ServiceType
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
    api_instance = ansible.module_utils.appliance_api_client.ConfigApi(api_client)
    service_type = ansible.module_utils.appliance_api_client.ServiceType() # ServiceType | Service Type

    try:
        # Get the custom template for a service.
        api_response = api_instance.config_advanced_service_customization_template_get(service_type)
        print("The response of ConfigApi->config_advanced_service_customization_template_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->config_advanced_service_customization_template_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_type** | [**ServiceType**](.md)| Service Type | 

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
**200** | success |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_advanced_service_customization_template_put**
> ConfigServiceCustomizationResponseJson config_advanced_service_customization_template_put(service_type, body)

Put a custom template for a service.

Put a new custom template for a service, along with its state.

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.config_service_customization_response_json import ConfigServiceCustomizationResponseJson
from ansible.module_utils.appliance_api_client.models.service_type import ServiceType
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
    api_instance = ansible.module_utils.appliance_api_client.ConfigApi(api_client)
    service_type = ansible.module_utils.appliance_api_client.ServiceType() # ServiceType | Service Type
    body = 'body_example' # str | The custom service template to be pushed to the appliance.

    try:
        # Put a custom template for a service.
        api_response = api_instance.config_advanced_service_customization_template_put(service_type, body)
        print("The response of ConfigApi->config_advanced_service_customization_template_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->config_advanced_service_customization_template_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_type** | [**ServiceType**](.md)| Service Type | 
 **body** | **str**| The custom service template to be pushed to the appliance. | 

### Return type

[**ConfigServiceCustomizationResponseJson**](ConfigServiceCustomizationResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_get**
> ConfigGetResponseJson config_get(if_none_match=if_none_match, suppress_secrets=suppress_secrets)

Get the current configuration

Get the currently active appliance configuration.

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.config_get_response_json import ConfigGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.ConfigApi(api_client)
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
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.config_put_request import ConfigPutRequest
from ansible.module_utils.appliance_api_client.models.config_put_response_json import ConfigPutResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.ConfigApi(api_client)
    config_put_request = ansible.module_utils.appliance_api_client.ConfigPutRequest() # ConfigPutRequest | The config to be pushed to the appliance.
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
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.config_post_response_json import ConfigPostResponseJson
from ansible.module_utils.appliance_api_client.models.config_put_request import ConfigPutRequest
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
    api_instance = ansible.module_utils.appliance_api_client.ConfigApi(api_client)
    config_put_request = ansible.module_utils.appliance_api_client.ConfigPutRequest() # ConfigPutRequest | The config to be validated.
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

