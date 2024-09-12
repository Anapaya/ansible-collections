# openapi_client.InitApi

All URIs are relative to *http://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_put**](InitApi.md#config_put) | **PUT** /config | Put a new configuration
[**config_validate_post**](InitApi.md#config_validate_post) | **POST** /config/validate | Validates a configuration
[**cppki_certificates_post**](InitApi.md#cppki_certificates_post) | **POST** /cppki/certificates | Add an AS certificate chain
[**cppki_csrs_post**](InitApi.md#cppki_csrs_post) | **POST** /cppki/csrs | Create an AS certificate signing request
[**cppki_trcs_bundle_post**](InitApi.md#cppki_trcs_bundle_post) | **POST** /cppki/trcs/bundle | Add a bundle of TRC files
[**cppki_trcs_post**](InitApi.md#cppki_trcs_post) | **POST** /cppki/trcs | Add a TRC file


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
    api_instance = openapi_client.InitApi(api_client)
    config_put_request = openapi_client.ConfigPutRequest() # ConfigPutRequest | The config to be pushed to the appliance.
    if_match = 'if_match_example' # str |  (optional)
    force = True # bool | Push the configuration, even if configuration validation fails. This parameter MUST be used with care as it can leave the appliance in a misconfigured state. (optional)
    disable_strict_parsing = True # bool | Disable strict parsing of the appliance configuration. (optional)

    try:
        # Put a new configuration
        api_response = api_instance.config_put(config_put_request, if_match=if_match, force=force, disable_strict_parsing=disable_strict_parsing)
        print("The response of InitApi->config_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitApi->config_put: %s\n" % e)
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
    api_instance = openapi_client.InitApi(api_client)
    config_put_request = openapi_client.ConfigPutRequest() # ConfigPutRequest | The config to be validated.
    disable_strict_parsing = True # bool | Disable strict parsing of the appliance configuration. (optional)

    try:
        # Validates a configuration
        api_response = api_instance.config_validate_post(config_put_request, disable_strict_parsing=disable_strict_parsing)
        print("The response of InitApi->config_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitApi->config_validate_post: %s\n" % e)
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

# **cppki_certificates_post**
> CppkiCertificatesPostResponseJson cppki_certificates_post(body, force=force)

Add an AS certificate chain

Add a SCION CPPKI AS certificate chain to the device by promoting an existing certificate signing request. The certificate chain is first verified against the active TRC of the local ISD before it is added. Only verifiable certificate chains are added.  Use the 'force' query parameter to force the addition of the certificate chain regardless of validity or verifiability. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.cppki_certificates_post_response_json import CppkiCertificatesPostResponseJson
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
    api_instance = openapi_client.InitApi(api_client)
    body = None # bytearray | 
    force = False # bool | If force is true the certificate chain is added regardless of validity.  (optional) (default to False)

    try:
        # Add an AS certificate chain
        api_response = api_instance.cppki_certificates_post(body, force=force)
        print("The response of InitApi->cppki_certificates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitApi->cppki_certificates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 
 **force** | **bool**| If force is true the certificate chain is added regardless of validity.  | [optional] [default to False]

### Return type

[**CppkiCertificatesPostResponseJson**](CppkiCertificatesPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/pkcs7-mime, application/x-pem-files
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_csrs_post**
> CppkiCsrsPostResponseJson cppki_csrs_post(certificate_signing_request)

Create an AS certificate signing request

Create a SCION CPPKI AS Certificate Signing Request (CSR). The CSR needs to be signed by a SCION CPPKI Certificate Authority in the local ISD. The fully signed certificate chain then needs to be installed via the /cppki/certificates endpoint. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.certificate_signing_request import CertificateSigningRequest
from openapi_client.models.cppki_csrs_post_response_json import CppkiCsrsPostResponseJson
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
    api_instance = openapi_client.InitApi(api_client)
    certificate_signing_request = openapi_client.CertificateSigningRequest() # CertificateSigningRequest | The parameters for the CSR. 

    try:
        # Create an AS certificate signing request
        api_response = api_instance.cppki_csrs_post(certificate_signing_request)
        print("The response of InitApi->cppki_csrs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitApi->cppki_csrs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_signing_request** | [**CertificateSigningRequest**](CertificateSigningRequest.md)| The parameters for the CSR.  | 

### Return type

[**CppkiCsrsPostResponseJson**](CppkiCsrsPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/x-pem-file, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_trcs_bundle_post**
> CppkiTrcsBundlePostResponseJson cppki_trcs_bundle_post(body, force=force)

Add a bundle of TRC files

Add a bundle SCION CPPKI Trust Root Configuration (TRC) files to the device. The TRCs are first validated before they are added to the trust store. Only valid TRCs are added to the trust store. Use the 'force' query parameter to force the addition of the TRCs regardless of validity. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.cppki_trcs_bundle_post_response_json import CppkiTrcsBundlePostResponseJson
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
    api_instance = openapi_client.InitApi(api_client)
    body = [B@75c5ab79 # bytearray | 
    force = False # bool | If force is true, the TRC is added regardless of validity. (optional) (default to False)

    try:
        # Add a bundle of TRC files
        api_response = api_instance.cppki_trcs_bundle_post(body, force=force)
        print("The response of InitApi->cppki_trcs_bundle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitApi->cppki_trcs_bundle_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 
 **force** | **bool**| If force is true, the TRC is added regardless of validity. | [optional] [default to False]

### Return type

[**CppkiTrcsBundlePostResponseJson**](CppkiTrcsBundlePostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-pem-files
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_trcs_post**
> CppkiTrcsPostResponseJson cppki_trcs_post(body, force=force)

Add a TRC file

Add a SCION CPPKI Trust Root Configuration (TRC) file to the device. The TRC is first validated before it is added to the trust store. Only valid TRCs are added to the trust store. Use the 'force' query parameter to force the addition of the TRC regardless of validity. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.cppki_trcs_post_response_json import CppkiTrcsPostResponseJson
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
    api_instance = openapi_client.InitApi(api_client)
    body = [B@35bfa7be # bytearray | 
    force = False # bool | If force is true, the TRC is added regardless of validity. (optional) (default to False)

    try:
        # Add a TRC file
        api_response = api_instance.cppki_trcs_post(body, force=force)
        print("The response of InitApi->cppki_trcs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InitApi->cppki_trcs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **bytearray**|  | 
 **force** | **bool**| If force is true, the TRC is added regardless of validity. | [optional] [default to False]

### Return type

[**CppkiTrcsPostResponseJson**](CppkiTrcsPostResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-pem-files
 - **Accept**: application/json, application/json+problem

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

