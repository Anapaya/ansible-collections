# openapi_client.SoftwareLicenseApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_license_features_get**](SoftwareLicenseApi.md#software_license_features_get) | **GET** /software/licenses/features | Get the feature set mapping.
[**software_license_features_put**](SoftwareLicenseApi.md#software_license_features_put) | **PUT** /software/licenses/features | Update the feature set mapping.
[**software_license_request_get**](SoftwareLicenseApi.md#software_license_request_get) | **GET** /software/licenses/request | Get the license request data.
[**software_license_status_get**](SoftwareLicenseApi.md#software_license_status_get) | **GET** /software/licenses/status | Get the status of the software license.
[**software_licenses_get**](SoftwareLicenseApi.md#software_licenses_get) | **GET** /software/licenses | Get the list of licenses present on the appliance.
[**software_licenses_id_delete**](SoftwareLicenseApi.md#software_licenses_id_delete) | **DELETE** /software/licenses/{id} | Delete a specific license.
[**software_licenses_id_get**](SoftwareLicenseApi.md#software_licenses_id_get) | **GET** /software/licenses/{id} | Get a specific license.
[**software_licenses_post**](SoftwareLicenseApi.md#software_licenses_post) | **POST** /software/licenses | Add a new license.


# **software_license_features_get**
> FeatureSetMapping software_license_features_get()

Get the feature set mapping.

Gets the feature set mapping. That defines for the different product tiers what features are available. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.feature_set_mapping import FeatureSetMapping
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)

    try:
        # Get the feature set mapping.
        api_response = api_instance.software_license_features_get()
        print("The response of SoftwareLicenseApi->software_license_features_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_license_features_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FeatureSetMapping**](FeatureSetMapping.md)

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

# **software_license_features_put**
> FeatureSetMapping software_license_features_put(software_license_features_put_request)

Update the feature set mapping.

Updates the feature set mapping. That defines for the different product tiers what features are available. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.feature_set_mapping import FeatureSetMapping
from openapi_client.models.software_license_features_put_request import SoftwareLicenseFeaturesPutRequest
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)
    software_license_features_put_request = openapi_client.SoftwareLicenseFeaturesPutRequest() # SoftwareLicenseFeaturesPutRequest | The feature set mapping.

    try:
        # Update the feature set mapping.
        api_response = api_instance.software_license_features_put(software_license_features_put_request)
        print("The response of SoftwareLicenseApi->software_license_features_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_license_features_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_license_features_put_request** | [**SoftwareLicenseFeaturesPutRequest**](SoftwareLicenseFeaturesPutRequest.md)| The feature set mapping. | 

### Return type

[**FeatureSetMapping**](FeatureSetMapping.md)

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

# **software_license_request_get**
> LicenseRequestGetResponseJson software_license_request_get()

Get the license request data.

Get the data for a license request for this specific appliance. The license request can be used to request a valid license from Anapaya for the given appliance. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.license_request_get_response_json import LicenseRequestGetResponseJson
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)

    try:
        # Get the license request data.
        api_response = api_instance.software_license_request_get()
        print("The response of SoftwareLicenseApi->software_license_request_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_license_request_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicenseRequestGetResponseJson**](LicenseRequestGetResponseJson.md)

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

# **software_license_status_get**
> LicenseStatusGetResponseJson software_license_status_get()

Get the status of the software license.

The status of the software license indicates whether a valid license is present, or whether the device runs in grace period or in restricted mode. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.license_status_get_response_json import LicenseStatusGetResponseJson
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)

    try:
        # Get the status of the software license.
        api_response = api_instance.software_license_status_get()
        print("The response of SoftwareLicenseApi->software_license_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_license_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicenseStatusGetResponseJson**](LicenseStatusGetResponseJson.md)

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

# **software_licenses_get**
> LicensesGetResponseJson software_licenses_get()

Get the list of licenses present on the appliance.

Get the list of licenses present on the appliance. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.licenses_get_response_json import LicensesGetResponseJson
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)

    try:
        # Get the list of licenses present on the appliance.
        api_response = api_instance.software_licenses_get()
        print("The response of SoftwareLicenseApi->software_licenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_licenses_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicensesGetResponseJson**](LicensesGetResponseJson.md)

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

# **software_licenses_id_delete**
> software_licenses_id_delete(id)

Delete a specific license.

Delete the license with the given ID. 

### Example


```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)
    id = 'id_example' # str | The license ID.

    try:
        # Delete a specific license.
        api_instance.software_licenses_id_delete(id)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_licenses_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The license ID. | 

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
**204** | License deleted |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_licenses_id_get**
> LicensePayloadJson software_licenses_id_get(id)

Get a specific license.

Get the license with the given ID. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.license_payload_json import LicensePayloadJson
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)
    id = 'id_example' # str | The license ID.

    try:
        # Get a specific license.
        api_response = api_instance.software_licenses_id_get(id)
        print("The response of SoftwareLicenseApi->software_licenses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_licenses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The license ID. | 

### Return type

[**LicensePayloadJson**](LicensePayloadJson.md)

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

# **software_licenses_post**
> LicensePayloadJson software_licenses_post(software_licenses_post_request)

Add a new license.

Add a new license to the appliance. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.license_payload_json import LicensePayloadJson
from openapi_client.models.software_licenses_post_request import SoftwareLicensesPostRequest
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
    api_instance = openapi_client.SoftwareLicenseApi(api_client)
    software_licenses_post_request = openapi_client.SoftwareLicensesPostRequest() # SoftwareLicensesPostRequest | The license to be pushed to the appliance.

    try:
        # Add a new license.
        api_response = api_instance.software_licenses_post(software_licenses_post_request)
        print("The response of SoftwareLicenseApi->software_licenses_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareLicenseApi->software_licenses_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **software_licenses_post_request** | [**SoftwareLicensesPostRequest**](SoftwareLicensesPostRequest.md)| The license to be pushed to the appliance. | 

### Return type

[**LicensePayloadJson**](LicensePayloadJson.md)

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

