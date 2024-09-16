# ansible.module_utils.appliance_api_client.CppkiApi

All URIs are relative to *https://localhost:443/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cppki_certificate_blob_get**](CppkiApi.md#cppki_certificate_blob_get) | **GET** /cppki/certificates/{chain_id}/blob | Get the certificate chain blob
[**cppki_certificate_get**](CppkiApi.md#cppki_certificate_get) | **GET** /cppki/certificates/{chain_id} | Get the certificate chain
[**cppki_certificates_get**](CppkiApi.md#cppki_certificates_get) | **GET** /cppki/certificates | List the certificate chains
[**cppki_certificates_post**](CppkiApi.md#cppki_certificates_post) | **POST** /cppki/certificates | Add an AS certificate chain
[**cppki_certificates_renew_post**](CppkiApi.md#cppki_certificates_renew_post) | **POST** /cppki/certificates/renew | Manually renew an AS certificate chain
[**cppki_certificates_request_post**](CppkiApi.md#cppki_certificates_request_post) | **POST** /cppki/certificates/request | Manually request an AS certificate chain for a given CSR
[**cppki_csr_blob_get**](CppkiApi.md#cppki_csr_blob_get) | **GET** /cppki/csrs/{csr_id}/blob | Get the certificate signing request blob
[**cppki_csr_get**](CppkiApi.md#cppki_csr_get) | **GET** /cppki/csrs/{csr_id} | Get the certificate signing request
[**cppki_csrs_get**](CppkiApi.md#cppki_csrs_get) | **GET** /cppki/csrs | List the certificate signing requests
[**cppki_csrs_post**](CppkiApi.md#cppki_csrs_post) | **POST** /cppki/csrs | Create an AS certificate signing request
[**cppki_trc_blob_get**](CppkiApi.md#cppki_trc_blob_get) | **GET** /cppki/trcs/isd{isd}-b{base}-s{serial}/blob | Get the TRC blob
[**cppki_trc_get**](CppkiApi.md#cppki_trc_get) | **GET** /cppki/trcs/isd{isd}-b{base}-s{serial} | Get the TRC
[**cppki_trcs_bundle_post**](CppkiApi.md#cppki_trcs_bundle_post) | **POST** /cppki/trcs/bundle | Add a bundle of TRC files
[**cppki_trcs_get**](CppkiApi.md#cppki_trcs_get) | **GET** /cppki/trcs | List the TRC files
[**cppki_trcs_post**](CppkiApi.md#cppki_trcs_post) | **POST** /cppki/trcs | Add a TRC file


# **cppki_certificate_blob_get**
> CppkiCertificateBlobGetResponseJson cppki_certificate_blob_get(chain_id)

Get the certificate chain blob

Get the SCION CPPKI AS certificate chain encoded as PEM bytes blob for a given ChainID. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_certificate_blob_get_response_json import CppkiCertificateBlobGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    chain_id = 'chain_id_example' # str | Certificate chain identifier.

    try:
        # Get the certificate chain blob
        api_response = api_instance.cppki_certificate_blob_get(chain_id)
        print("The response of CppkiApi->cppki_certificate_blob_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_certificate_blob_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Certificate chain identifier. | 

### Return type

[**CppkiCertificateBlobGetResponseJson**](CppkiCertificateBlobGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-pem-file, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate chain blob |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_certificate_get**
> CppkiCertificateGetResponseJson cppki_certificate_get(chain_id)

Get the certificate chain

Get the SCION CPPKI AS certificate chain for a given ChainID. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_certificate_get_response_json import CppkiCertificateGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    chain_id = 'chain_id_example' # str | Certificate chain identifier.

    try:
        # Get the certificate chain
        api_response = api_instance.cppki_certificate_get(chain_id)
        print("The response of CppkiApi->cppki_certificate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_certificate_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain_id** | **str**| Certificate chain identifier. | 

### Return type

[**CppkiCertificateGetResponseJson**](CppkiCertificateGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate chain |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_certificates_get**
> CppkiCertificatesGetResponseJson cppki_certificates_get(isd_as=isd_as, all=all)

List the certificate chains

List the certificate chains that are available on the device. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_certificates_get_response_json import CppkiCertificatesGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    isd_as = 'isd_as_example' # str |  (optional)
    all = True # bool | Include all certificate chains instead of just the valid ones. (optional)

    try:
        # List the certificate chains
        api_response = api_instance.cppki_certificates_get(isd_as=isd_as, all=all)
        print("The response of CppkiApi->cppki_certificates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_certificates_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isd_as** | **str**|  | [optional] 
 **all** | **bool**| Include all certificate chains instead of just the valid ones. | [optional] 

### Return type

[**CppkiCertificatesGetResponseJson**](CppkiCertificatesGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
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
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_certificates_post_response_json import CppkiCertificatesPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    body = None # bytearray | 
    force = False # bool | If force is true the certificate chain is added regardless of validity.  (optional) (default to False)

    try:
        # Add an AS certificate chain
        api_response = api_instance.cppki_certificates_post(body, force=force)
        print("The response of CppkiApi->cppki_certificates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_certificates_post: %s\n" % e)
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

# **cppki_certificates_renew_post**
> cppki_certificates_renew_post(cppki_certificates_renew_post_request, isd_as=isd_as)

Manually renew an AS certificate chain

Manually renew a SCION CPPKI AS certificate chain with the regular renewal mechanism. By default, the distinguished name of the subject in the predecessor certificate chain is used. A different distinguished name can be requested by setting the subject in the request body. By default the issuers are taken from the appliance configuration, specific issuers can be configured in the request body. If they are set, certificate renewal is attempted with each issuer in order until success.  Note that certificate renewal requires at least one valid certificate chain to be present on the appliance. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_certificates_renew_post_request import CppkiCertificatesRenewPostRequest
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    cppki_certificates_renew_post_request = ansible.module_utils.appliance_api_client.CppkiCertificatesRenewPostRequest() # CppkiCertificatesRenewPostRequest | 
    isd_as = 'isd_as_example' # str | The ISD-AS for which the certificate is renewed. This parameter is required only if the request body is not set, and there are multiple ISD-ASes configured on the appliance.  (optional)

    try:
        # Manually renew an AS certificate chain
        api_instance.cppki_certificates_renew_post(cppki_certificates_renew_post_request, isd_as=isd_as)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_certificates_renew_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cppki_certificates_renew_post_request** | [**CppkiCertificatesRenewPostRequest**](CppkiCertificatesRenewPostRequest.md)|  | 
 **isd_as** | **str**| The ISD-AS for which the certificate is renewed. This parameter is required only if the request body is not set, and there are multiple ISD-ASes configured on the appliance.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-pem-file, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_certificates_request_post**
> cppki_certificates_request_post(cppki_certificates_request_post_request)

Manually request an AS certificate chain for a given CSR

Manually request a SCION CPPKI AS certificate chain for a given CSR using the regular certificate renewal mechanism. The endpoint expects a CSR and uses that to request a certificate renewal. The certificate renewal request is signed by an active key/certificate of the appliance such that the CA will be able to authenticate the renewal request and issue the certificate. This is useful if one appliance has been disconnected from the SCION network for several days and thus has no valid AS certificate anymore that could be used for certificate renewal. In such a case, one can generate a new CSR on the appliance that was offline and use this endpoint on an appliance that still has a valid AS certificate to request a new certificate on behalf of the sibling.The returned certificate can then be deployed to the offline appliance using the regular `POST /cppki/certificates` endpoint. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_certificates_request_post_request import CppkiCertificatesRequestPostRequest
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    cppki_certificates_request_post_request = ansible.module_utils.appliance_api_client.CppkiCertificatesRequestPostRequest() # CppkiCertificatesRequestPostRequest | 

    try:
        # Manually request an AS certificate chain for a given CSR
        api_instance.cppki_certificates_request_post(cppki_certificates_request_post_request)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_certificates_request_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cppki_certificates_request_post_request** | [**CppkiCertificatesRequestPostRequest**](CppkiCertificatesRequestPostRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x-pem-file, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_csr_blob_get**
> CppkiCsrBlobGetResponseJson cppki_csr_blob_get(csr_id)

Get the certificate signing request blob

Get the SCION CPPKI Certificate Signing Request encoded as PEM bytes blob for a given CSR ID. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_csr_blob_get_response_json import CppkiCsrBlobGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    csr_id = 'csr_id_example' # str | Certificate signing request identifier.

    try:
        # Get the certificate signing request blob
        api_response = api_instance.cppki_csr_blob_get(csr_id)
        print("The response of CppkiApi->cppki_csr_blob_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_csr_blob_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| Certificate signing request identifier. | 

### Return type

[**CppkiCsrBlobGetResponseJson**](CppkiCsrBlobGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-pem-file, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate signing request blob |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_csr_get**
> CppkiCsrGetResponseJson cppki_csr_get(csr_id)

Get the certificate signing request

Get the SCION Certificate Signing Request for a given CSR ID 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_csr_get_response_json import CppkiCsrGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    csr_id = 'csr_id_example' # str | Certificate signing request identifier.

    try:
        # Get the certificate signing request
        api_response = api_instance.cppki_csr_get(csr_id)
        print("The response of CppkiApi->cppki_csr_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_csr_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csr_id** | **str**| Certificate signing request identifier. | 

### Return type

[**CppkiCsrGetResponseJson**](CppkiCsrGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Certificate signing request |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_csrs_get**
> CppkiCsrsGetResponseJson cppki_csrs_get(isd_as=isd_as)

List the certificate signing requests

List the certificate signing requests that are available on the device. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_csrs_get_response_json import CppkiCsrsGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    isd_as = 'isd_as_example' # str |  (optional)

    try:
        # List the certificate signing requests
        api_response = api_instance.cppki_csrs_get(isd_as=isd_as)
        print("The response of CppkiApi->cppki_csrs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_csrs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isd_as** | **str**|  | [optional] 

### Return type

[**CppkiCsrsGetResponseJson**](CppkiCsrsGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.certificate_signing_request import CertificateSigningRequest
from ansible.module_utils.appliance_api_client.models.cppki_csrs_post_response_json import CppkiCsrsPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    certificate_signing_request = ansible.module_utils.appliance_api_client.CertificateSigningRequest() # CertificateSigningRequest | The parameters for the CSR. 

    try:
        # Create an AS certificate signing request
        api_response = api_instance.cppki_csrs_post(certificate_signing_request)
        print("The response of CppkiApi->cppki_csrs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_csrs_post: %s\n" % e)
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

# **cppki_trc_blob_get**
> CppkiTrcBlobGetResponseJson cppki_trc_blob_get(isd, base, serial)

Get the TRC blob

Get the SCION CPPKI Trust Root Configuration (TRC) as PEM encoded byte blob. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_trc_blob_get_response_json import CppkiTrcBlobGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    isd = 12 # int | 
    base = 1 # int | 
    serial = 3 # int | 

    try:
        # Get the TRC blob
        api_response = api_instance.cppki_trc_blob_get(isd, base, serial)
        print("The response of CppkiApi->cppki_trc_blob_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_trc_blob_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isd** | **int**|  | 
 **base** | **int**|  | 
 **serial** | **int**|  | 

### Return type

[**CppkiTrcBlobGetResponseJson**](CppkiTrcBlobGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-pem-file, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
**500** | internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cppki_trc_get**
> CppkiTrcGetResponseJson cppki_trc_get(isd, base, serial)

Get the TRC

Get the SCION CPPKI Trust Root Configuration (TRC). 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_trc_get_response_json import CppkiTrcGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    isd = 12 # int | 
    base = 1 # int | 
    serial = 3 # int | 

    try:
        # Get the TRC
        api_response = api_instance.cppki_trc_get(isd, base, serial)
        print("The response of CppkiApi->cppki_trc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_trc_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isd** | **int**|  | 
 **base** | **int**|  | 
 **serial** | **int**|  | 

### Return type

[**CppkiTrcGetResponseJson**](CppkiTrcGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+problem

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | bad request |  -  |
**404** | not found |  -  |
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
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_trcs_bundle_post_response_json import CppkiTrcsBundlePostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    body = [B@4a0dd851 # bytearray | 
    force = False # bool | If force is true, the TRC is added regardless of validity. (optional) (default to False)

    try:
        # Add a bundle of TRC files
        api_response = api_instance.cppki_trcs_bundle_post(body, force=force)
        print("The response of CppkiApi->cppki_trcs_bundle_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_trcs_bundle_post: %s\n" % e)
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

# **cppki_trcs_get**
> CppkiTrcsGetResponseJson cppki_trcs_get(isd=isd, all=all)

List the TRC files

List the latest SCION CPPKI Trust Root Configuration (TRC) files for each ISD that are known to the appliance. The result can be filtered by ISD. Optionally, all TRCs can be requested instead of only the latest ones by setting the 'all' query parameter. 

### Example

```python
import time
import os
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_trcs_get_response_json import CppkiTrcsGetResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    isd = [56] # List[int] | Comma-separated list of ISDs to include. (optional)
    all = True # bool | Include all TRCs instead of just the latest one per ISD. (optional)

    try:
        # List the TRC files
        api_response = api_instance.cppki_trcs_get(isd=isd, all=all)
        print("The response of CppkiApi->cppki_trcs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_trcs_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isd** | [**List[int]**](int.md)| Comma-separated list of ISDs to include. | [optional] 
 **all** | **bool**| Include all TRCs instead of just the latest one per ISD. | [optional] 

### Return type

[**CppkiTrcsGetResponseJson**](CppkiTrcsGetResponseJson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import ansible.module_utils.appliance_api_client
from ansible.module_utils.appliance_api_client.models.cppki_trcs_post_response_json import CppkiTrcsPostResponseJson
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
    api_instance = ansible.module_utils.appliance_api_client.CppkiApi(api_client)
    body = [B@3152d449 # bytearray | 
    force = False # bool | If force is true, the TRC is added regardless of validity. (optional) (default to False)

    try:
        # Add a TRC file
        api_response = api_instance.cppki_trcs_post(body, force=force)
        print("The response of CppkiApi->cppki_trcs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CppkiApi->cppki_trcs_post: %s\n" % e)
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

