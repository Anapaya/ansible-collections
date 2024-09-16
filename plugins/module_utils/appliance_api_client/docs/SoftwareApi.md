# ansible.module_utils.appliance_api_client.SoftwareApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_scion_install_get**](SoftwareApi.md#software_scion_install_get) | **GET** /software/scion/install/{id} | Get the status of the scion package installation process for the given id.
[**software_scion_install_post**](SoftwareApi.md#software_scion_install_post) | **POST** /software/scion/install | Trigger installation of the specified scion package.
[**software_scion_installed_get**](SoftwareApi.md#software_scion_installed_get) | **GET** /software/scion/installed | Get the installed scion version.
[**software_scion_package_fetch_get**](SoftwareApi.md#software_scion_package_fetch_get) | **GET** /software/scion/fetch/{id} | Get the download status of a software scion package.
[**software_scion_package_fetch_post**](SoftwareApi.md#software_scion_package_fetch_post) | **POST** /software/scion/fetch | Fetch the software scion package of a given version.
[**software_scion_package_local_delete**](SoftwareApi.md#software_scion_package_local_delete) | **DELETE** /software/scion/packages/local/{version} | Delete the given scion package.
[**software_scion_package_local_get**](SoftwareApi.md#software_scion_package_local_get) | **GET** /software/scion/packages/local/{version} | Get the scion package information.
[**software_scion_package_remote_get**](SoftwareApi.md#software_scion_package_remote_get) | **GET** /software/scion/packages/remote/{version} | Get the scion package information.
[**software_scion_packages_local_get**](SoftwareApi.md#software_scion_packages_local_get) | **GET** /software/scion/packages/local | List the package information for scion packages available locally.
[**software_scion_packages_local_post**](SoftwareApi.md#software_scion_packages_local_post) | **POST** /software/scion/packages/local | Upload the scion package.
[**software_scion_packages_remote_get**](SoftwareApi.md#software_scion_packages_remote_get) | **GET** /software/scion/packages/remote | List the package information for scion packages in the remote repository.
[**software_system_install_get**](SoftwareApi.md#software_system_install_get) | **GET** /software/system/install/{id} | Get the status of the system package installation process for the given id.
[**software_system_install_post**](SoftwareApi.md#software_system_install_post) | **POST** /software/system/install | Trigger installation of the specified system package.
[**software_system_installed_get**](SoftwareApi.md#software_system_installed_get) | **GET** /software/system/installed | Get the installed system version.
[**software_system_package_fetch_get**](SoftwareApi.md#software_system_package_fetch_get) | **GET** /software/system/fetch/{id} | Get the download status of a software system package.
[**software_system_package_fetch_post**](SoftwareApi.md#software_system_package_fetch_post) | **POST** /software/system/fetch | Fetch the software system package for a given version.
[**software_system_package_local_delete**](SoftwareApi.md#software_system_package_local_delete) | **DELETE** /software/system/packages/local/{version} | Delete the given system package.
[**software_system_package_local_get**](SoftwareApi.md#software_system_package_local_get) | **GET** /software/system/packages/local/{version} | Get the system package information.
[**software_system_package_remote_get**](SoftwareApi.md#software_system_package_remote_get) | **GET** /software/system/packages/remote/{version} | Get the system package information.
[**software_system_packages_local_get**](SoftwareApi.md#software_system_packages_local_get) | **GET** /software/system/packages/local | List the package information for system packages available locally.
[**software_system_packages_local_post**](SoftwareApi.md#software_system_packages_local_post) | **POST** /software/system/packages/local | Upload the system package.
[**software_system_packages_remote_get**](SoftwareApi.md#software_system_packages_remote_get) | **GET** /software/system/packages/remote | List the package information for system packages in the remote repository.


# **software_scion_install_get**
> SoftwareInstallGetResponseJson software_scion_install_get(id)

Get the status of the scion package installation process for the given id.

Get the status of the installation process of the scion package for the given id. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_install_get_response_json import SoftwareInstallGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    id = 'id_example' # str | Identifier of the installation process for the specific scion package version. 

    try:
        # Get the status of the scion package installation process for the given id.
        api_response = api_instance.software_scion_install_get(id)
        print("The response of SoftwareApi->software_scion_install_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_install_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the installation process for the specific scion package version.  | 

### Return type

[**SoftwareInstallGetResponseJson**](SoftwareInstallGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation status. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_install_post**
> SoftwareInstallPostResponseJson software_scion_install_post(software_install_post_request_json)

Trigger installation of the specified scion package.

Trigger the installation of the scion package with the version specified in the request body. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_install_post_request_json import SoftwareInstallPostRequestJson
from ansible.module_utils.appliance_api_client.models.software_install_post_response_json import SoftwareInstallPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    software_install_post_request_json = ansible.module_utils.appliance_api_client.SoftwareInstallPostRequestJson() # SoftwareInstallPostRequestJson | 

    try:
        # Trigger installation of the specified scion package.
        api_response = api_instance.software_scion_install_post(software_install_post_request_json)
        print("The response of SoftwareApi->software_scion_install_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_install_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_install_post_request_json** | [**SoftwareInstallPostRequestJson**](SoftwareInstallPostRequestJson.md)|  | 

### Return type

[**SoftwareInstallPostResponseJson**](SoftwareInstallPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Package version and installation ID. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**409** | request in conflict with current server state |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_installed_get**
> SoftwareInstalledGetResponseJson software_scion_installed_get()

Get the installed scion version.

Get the version of scion package currently installed. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_installed_get_response_json import SoftwareInstalledGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)

    try:
        # Get the installed scion version.
        api_response = api_instance.software_scion_installed_get()
        print("The response of SoftwareApi->software_scion_installed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_installed_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwareInstalledGetResponseJson**](SoftwareInstalledGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed scion version. |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_package_fetch_get**
> SoftwarePackageFetchGetResponseJson software_scion_package_fetch_get(id)

Get the download status of a software scion package.

Get the download status of a software scion package from a remote repository. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_fetch_get_response_json import SoftwarePackageFetchGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    id = 'id_example' # str | Identifier of the fetch process for the specific scion package version.

    try:
        # Get the download status of a software scion package.
        api_response = api_instance.software_scion_package_fetch_get(id)
        print("The response of SoftwareApi->software_scion_package_fetch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_package_fetch_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the fetch process for the specific scion package version. | 

### Return type

[**SoftwarePackageFetchGetResponseJson**](SoftwarePackageFetchGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetch status. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_package_fetch_post**
> SoftwarePackageFetchPostResponseJson software_scion_package_fetch_post(software_package_fetch_post_request_json)

Fetch the software scion package of a given version.

Fetch the software scion package of a given version from a remote repository. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_fetch_post_request_json import SoftwarePackageFetchPostRequestJson
from ansible.module_utils.appliance_api_client.models.software_package_fetch_post_response_json import SoftwarePackageFetchPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    software_package_fetch_post_request_json = ansible.module_utils.appliance_api_client.SoftwarePackageFetchPostRequestJson() # SoftwarePackageFetchPostRequestJson | 

    try:
        # Fetch the software scion package of a given version.
        api_response = api_instance.software_scion_package_fetch_post(software_package_fetch_post_request_json)
        print("The response of SoftwareApi->software_scion_package_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_package_fetch_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_package_fetch_post_request_json** | [**SoftwarePackageFetchPostRequestJson**](SoftwarePackageFetchPostRequestJson.md)|  | 

### Return type

[**SoftwarePackageFetchPostResponseJson**](SoftwarePackageFetchPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Package version and fetch ID. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**409** | request in conflict with current server state |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_package_local_delete**
> SoftwarePackageDeleteResponseJson software_scion_package_local_delete(version)

Delete the given scion package.

Delete the scion package for the given version if it is available locally on the appliance. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_delete_response_json import SoftwarePackageDeleteResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    version = 'version_example' # str | Version of the scion package.

    try:
        # Delete the given scion package.
        api_response = api_instance.software_scion_package_local_delete(version)
        print("The response of SoftwareApi->software_scion_package_local_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_package_local_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the scion package. | 

### Return type

[**SoftwarePackageDeleteResponseJson**](SoftwarePackageDeleteResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package information. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_package_local_get**
> SoftwarePackageGetResponseJson software_scion_package_local_get(version)

Get the scion package information.

Get the package information of the scion package for the given version. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_get_response_json import SoftwarePackageGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    version = 'version_example' # str | Version of the scion package.

    try:
        # Get the scion package information.
        api_response = api_instance.software_scion_package_local_get(version)
        print("The response of SoftwareApi->software_scion_package_local_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_package_local_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the scion package. | 

### Return type

[**SoftwarePackageGetResponseJson**](SoftwarePackageGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package information. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_package_remote_get**
> SoftwarePackageGetResponseJson software_scion_package_remote_get(version)

Get the scion package information.

Get the package information of the scion package for the given version. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_get_response_json import SoftwarePackageGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    version = 'version_example' # str | Version of the scion package.

    try:
        # Get the scion package information.
        api_response = api_instance.software_scion_package_remote_get(version)
        print("The response of SoftwareApi->software_scion_package_remote_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_package_remote_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the scion package. | 

### Return type

[**SoftwarePackageGetResponseJson**](SoftwarePackageGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package information. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_packages_local_get**
> SoftwarePackagesGetResponseJson software_scion_packages_local_get()

List the package information for scion packages available locally.

List the package information (e.g., version) for all the scion packages which are available locally on the appliance. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_packages_get_response_json import SoftwarePackagesGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)

    try:
        # List the package information for scion packages available locally.
        api_response = api_instance.software_scion_packages_local_get()
        print("The response of SoftwareApi->software_scion_packages_local_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_packages_local_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwarePackagesGetResponseJson**](SoftwarePackagesGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_packages_local_post**
> SoftwarePackagesPostResponseJson software_scion_packages_local_post(body, force=force)

Upload the scion package.

Upload the scion package to the local repository of the appliance.

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_packages_post_response_json import SoftwarePackagesPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    body = None # bytearray | 
    force = False # bool | If force is true, the package is stored regardless of whether it already exists. (optional) (default to False)

    try:
        # Upload the scion package.
        api_response = api_instance.software_scion_packages_local_post(body, force=force)
        print("The response of SoftwareApi->software_scion_packages_local_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_packages_local_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 
 **force** | **bool**| If force is true, the package is stored regardless of whether it already exists. | [optional] [default to False]

### Return type

[**SoftwarePackagesPostResponseJson**](SoftwarePackagesPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Package information. |  -  |
**400** | bad request |  -  |
**409** | request in conflict with current server state |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_scion_packages_remote_get**
> SoftwarePackagesGetResponseJson software_scion_packages_remote_get()

List the package information for scion packages in the remote repository.

List the package information (e.g., version) for all the scion packages which are available in the remote repository. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_packages_get_response_json import SoftwarePackagesGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)

    try:
        # List the package information for scion packages in the remote repository.
        api_response = api_instance.software_scion_packages_remote_get()
        print("The response of SoftwareApi->software_scion_packages_remote_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_scion_packages_remote_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwarePackagesGetResponseJson**](SoftwarePackagesGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_install_get**
> SoftwareInstallGetResponseJson software_system_install_get(id)

Get the status of the system package installation process for the given id.

Get the status of the installation process of the system package for the given id. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_install_get_response_json import SoftwareInstallGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    id = 'id_example' # str | Identifier of the installation process for the specific system package version. 

    try:
        # Get the status of the system package installation process for the given id.
        api_response = api_instance.software_system_install_get(id)
        print("The response of SoftwareApi->software_system_install_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_install_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the installation process for the specific system package version.  | 

### Return type

[**SoftwareInstallGetResponseJson**](SoftwareInstallGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installation status. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_install_post**
> SoftwareInstallPostResponseJson software_system_install_post(software_install_post_request_json)

Trigger installation of the specified system package.

Trigger the installation of the system package with the version specified in the request body. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_install_post_request_json import SoftwareInstallPostRequestJson
from ansible.module_utils.appliance_api_client.models.software_install_post_response_json import SoftwareInstallPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    software_install_post_request_json = ansible.module_utils.appliance_api_client.SoftwareInstallPostRequestJson() # SoftwareInstallPostRequestJson | 

    try:
        # Trigger installation of the specified system package.
        api_response = api_instance.software_system_install_post(software_install_post_request_json)
        print("The response of SoftwareApi->software_system_install_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_install_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_install_post_request_json** | [**SoftwareInstallPostRequestJson**](SoftwareInstallPostRequestJson.md)|  | 

### Return type

[**SoftwareInstallPostResponseJson**](SoftwareInstallPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Package version and installation ID. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**409** | request in conflict with current server state |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_installed_get**
> SoftwareInstalledGetResponseJson software_system_installed_get()

Get the installed system version.

Get the version of system package currently installed. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_installed_get_response_json import SoftwareInstalledGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)

    try:
        # Get the installed system version.
        api_response = api_instance.software_system_installed_get()
        print("The response of SoftwareApi->software_system_installed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_installed_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwareInstalledGetResponseJson**](SoftwareInstalledGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed system version. |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_package_fetch_get**
> SoftwarePackageFetchGetResponseJson software_system_package_fetch_get(id)

Get the download status of a software system package.

Get the download status of a software system package from a remote repository. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_fetch_get_response_json import SoftwarePackageFetchGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    id = 'id_example' # str | Identifier of the fetch process for the specific system package version.

    try:
        # Get the download status of a software system package.
        api_response = api_instance.software_system_package_fetch_get(id)
        print("The response of SoftwareApi->software_system_package_fetch_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_package_fetch_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the fetch process for the specific system package version. | 

### Return type

[**SoftwarePackageFetchGetResponseJson**](SoftwarePackageFetchGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetch status. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_package_fetch_post**
> SoftwarePackageFetchPostResponseJson software_system_package_fetch_post(software_package_fetch_post_request_json)

Fetch the software system package for a given version.

Fetch the software system package for a given version from a remote repository. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_fetch_post_request_json import SoftwarePackageFetchPostRequestJson
from ansible.module_utils.appliance_api_client.models.software_package_fetch_post_response_json import SoftwarePackageFetchPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    software_package_fetch_post_request_json = ansible.module_utils.appliance_api_client.SoftwarePackageFetchPostRequestJson() # SoftwarePackageFetchPostRequestJson | 

    try:
        # Fetch the software system package for a given version.
        api_response = api_instance.software_system_package_fetch_post(software_package_fetch_post_request_json)
        print("The response of SoftwareApi->software_system_package_fetch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_package_fetch_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_package_fetch_post_request_json** | [**SoftwarePackageFetchPostRequestJson**](SoftwarePackageFetchPostRequestJson.md)|  | 

### Return type

[**SoftwarePackageFetchPostResponseJson**](SoftwarePackageFetchPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Package version and fetch ID. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**409** | request in conflict with current server state |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_package_local_delete**
> SoftwarePackageDeleteResponseJson software_system_package_local_delete(version)

Delete the given system package.

Delete the system package for the given version if it is available locally on the appliance. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_delete_response_json import SoftwarePackageDeleteResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    version = 'version_example' # str | Version of the system package.

    try:
        # Delete the given system package.
        api_response = api_instance.software_system_package_local_delete(version)
        print("The response of SoftwareApi->software_system_package_local_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_package_local_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the system package. | 

### Return type

[**SoftwarePackageDeleteResponseJson**](SoftwarePackageDeleteResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package information. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_package_local_get**
> SoftwarePackageGetResponseJson software_system_package_local_get(version)

Get the system package information.

Get the package information of the system package for the given version. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_get_response_json import SoftwarePackageGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    version = 'version_example' # str | Version of the system package.

    try:
        # Get the system package information.
        api_response = api_instance.software_system_package_local_get(version)
        print("The response of SoftwareApi->software_system_package_local_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_package_local_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the system package. | 

### Return type

[**SoftwarePackageGetResponseJson**](SoftwarePackageGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package information. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_package_remote_get**
> SoftwarePackageGetResponseJson software_system_package_remote_get(version)

Get the system package information.

Get the package information of the system package for the given version. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_package_get_response_json import SoftwarePackageGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    version = 'version_example' # str | Version of the system package.

    try:
        # Get the system package information.
        api_response = api_instance.software_system_package_remote_get(version)
        print("The response of SoftwareApi->software_system_package_remote_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_package_remote_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Version of the system package. | 

### Return type

[**SoftwarePackageGetResponseJson**](SoftwarePackageGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Package information. |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_packages_local_get**
> SoftwarePackagesGetResponseJson software_system_packages_local_get()

List the package information for system packages available locally.

List the package information (e.g., version) for all the system packages which are available locally on the appliance. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_packages_get_response_json import SoftwarePackagesGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)

    try:
        # List the package information for system packages available locally.
        api_response = api_instance.software_system_packages_local_get()
        print("The response of SoftwareApi->software_system_packages_local_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_packages_local_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwarePackagesGetResponseJson**](SoftwarePackagesGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_packages_local_post**
> SoftwarePackagesPostResponseJson software_system_packages_local_post(body, force=force)

Upload the system package.

Upload the system package to the local repository of the appliance.

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_packages_post_response_json import SoftwarePackagesPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)
    body = None # bytearray | 
    force = False # bool | If force is true, the package is stored regardless of whether it already exists. (optional) (default to False)

    try:
        # Upload the system package.
        api_response = api_instance.software_system_packages_local_post(body, force=force)
        print("The response of SoftwareApi->software_system_packages_local_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_packages_local_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 
 **force** | **bool**| If force is true, the package is stored regardless of whether it already exists. | [optional] [default to False]

### Return type

[**SoftwarePackagesPostResponseJson**](SoftwarePackagesPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Package information. |  -  |
**400** | bad request |  -  |
**409** | request in conflict with current server state |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_system_packages_remote_get**
> SoftwarePackagesGetResponseJson software_system_packages_remote_get()

List the package information for system packages in the remote repository.

List the package information (e.g., version) for all the system packages which are available in the remote repository. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.software_packages_get_response_json import SoftwarePackagesGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.SoftwareApi(api_client)

    try:
        # List the package information for system packages in the remote repository.
        api_response = api_instance.software_system_packages_remote_get()
        print("The response of SoftwareApi->software_system_packages_remote_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareApi->software_system_packages_remote_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SoftwarePackagesGetResponseJson**](SoftwarePackagesGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

