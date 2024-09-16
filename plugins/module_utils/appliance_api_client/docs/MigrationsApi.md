# ansible.module_utils.appliance_api_client.MigrationsApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrations_config_get**](MigrationsApi.md#migrations_config_get) | **GET** /migrations/{version}/config | Get the configuration for migration to {version}.
[**migrations_config_put**](MigrationsApi.md#migrations_config_put) | **PUT** /migrations/{version}/config | Put the configuration for migration to {version}.


# **migrations_config_get**
> migrations_config_get(version)

Get the configuration for migration to {version}.

Get the configuration that is applied on the migration to version {version}. 

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
    api_instance = ansible.module_utils.appliance_api_client.MigrationsApi(api_client)
    version = 'version_example' # str | Version of the appliance for which the configuration is.

    try:
        # Get the configuration for migration to {version}.
        api_instance.migrations_config_get(version)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_config_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the appliance for which the configuration is. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration for the given version that was previously set. |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_config_put**
> migrations_config_put(version)

Put the configuration for migration to {version}.

This endpoint allows the preparation of the installation of a new appliance release. It accepts any json and stores this so that the new appliance version will find it. The new appliance version will validate the configuration and if validation succeeds use that as configuration. This helps to do upgrades where new configuration features can't be automatically migrated or are newly added. For example to migrate to v0.33.1 put the new configuration to /migrations/v0.33/config. Note that if there was a previous configuration it is overwritten. 

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
    api_instance = ansible.module_utils.appliance_api_client.MigrationsApi(api_client)
    version = 'version_example' # str | Version of the appliance for which the configuration is.

    try:
        # Put the configuration for migration to {version}.
        api_instance.migrations_config_put(version)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_config_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the appliance for which the configuration is. | 

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
**200** | Successfully put the configuration. |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

