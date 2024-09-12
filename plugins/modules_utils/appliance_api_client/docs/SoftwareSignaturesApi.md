# openapi_client.SoftwareSignaturesApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_keys**](SoftwareSignaturesApi.md#get_keys) | **GET** /software/keys | Get the public signing keys.
[**get_signatures**](SoftwareSignaturesApi.md#get_signatures) | **GET** /software/signatures/{type}/{version} | Get the specified signatures
[**post_keys**](SoftwareSignaturesApi.md#post_keys) | **POST** /software/keys | Install new public signing keys.
[**post_signatures**](SoftwareSignaturesApi.md#post_signatures) | **POST** /software/signatures/{type}/{version} | Install signatures.


# **get_keys**
> Keys get_keys()

Get the public signing keys.

Get the currently installed public  signing keys. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.keys import Keys
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
    api_instance = openapi_client.SoftwareSignaturesApi(api_client)

    try:
        # Get the public signing keys.
        api_response = api_instance.get_keys()
        print("The response of SoftwareSignaturesApi->get_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareSignaturesApi->get_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Keys**](Keys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public signing keys. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signatures**
> Signatures get_signatures(type, version)

Get the specified signatures

Get the specified signatures.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.signatures import Signatures
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
    api_instance = openapi_client.SoftwareSignaturesApi(api_client)
    type = 'type_example' # str | 
    version = 'version_example' # str | 

    try:
        # Get the specified signatures
        api_response = api_instance.get_signatures(type, version)
        print("The response of SoftwareSignaturesApi->get_signatures:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SoftwareSignaturesApi->get_signatures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**Signatures**](Signatures.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Signatures. |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_keys**
> post_keys(keys)

Install new public signing keys.

Install new public signing keys. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.keys import Keys
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
    api_instance = openapi_client.SoftwareSignaturesApi(api_client)
    keys = openapi_client.Keys() # Keys | 

    try:
        # Install new public signing keys.
        api_instance.post_keys(keys)
    except Exception as e:
        print("Exception when calling SoftwareSignaturesApi->post_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keys** | [**Keys**](Keys.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public signing keys. |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_signatures**
> post_signatures(type, version, signatures)

Install signatures.

Install signatures.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.signatures import Signatures
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
    api_instance = openapi_client.SoftwareSignaturesApi(api_client)
    type = 'type_example' # str | 
    version = 'version_example' # str | 
    signatures = openapi_client.Signatures() # Signatures | 

    try:
        # Install signatures.
        api_instance.post_signatures(type, version, signatures)
    except Exception as e:
        print("Exception when calling SoftwareSignaturesApi->post_signatures: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **version** | **str**|  | 
 **signatures** | [**Signatures**](Signatures.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public signing keys. |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |
**504** | gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

