# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: v0.37.1
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr, conlist

from typing import Optional

from ansible.module_utils.appliance_api_client.models.health_get_response_json import HealthGetResponseJson
from ansible.module_utils.appliance_api_client.models.health_status import HealthStatus

from ansible.module_utils.appliance_api_client.api_client import ApiClient
from ansible.module_utils.appliance_api_client.api_response import ApiResponse
from ansible.module_utils.appliance_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class HealthApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def health_get(self, check_id : Annotated[Optional[conlist(StrictStr)], Field(description="List of check_id (or check_id prefixes) that should be included in the response. If unset, health checks are not filtered by check_id. ")] = None, service_name : Annotated[Optional[conlist(StrictStr)], Field(description="List of service_name (or service_name prefixes) that should be included in the response. If unset, health checks are not filtered by service_name. ")] = None, status : Annotated[Optional[conlist(HealthStatus)], Field(description="List of status that should be included in the response. If unset, health checks are not filtered by status. ")] = None, **kwargs) -> HealthGetResponseJson:  # noqa: E501
        """Appliance Health  # noqa: E501

        Report the appliance health along with the executed health checks. The health status is based on a set of health checks that are executed. Check the documentation of the individual health checks for more information.  Note that the status is only based on the health checks that are part of the response. If you filter out non-passing health checks, the top level status will be reported as passing.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.health_get(check_id, service_name, status, async_req=True)
        >>> result = thread.get()

        :param check_id: List of check_id (or check_id prefixes) that should be included in the response. If unset, health checks are not filtered by check_id. 
        :type check_id: List[str]
        :param service_name: List of service_name (or service_name prefixes) that should be included in the response. If unset, health checks are not filtered by service_name. 
        :type service_name: List[str]
        :param status: List of status that should be included in the response. If unset, health checks are not filtered by status. 
        :type status: List[HealthStatus]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HealthGetResponseJson
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the health_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.health_get_with_http_info(check_id, service_name, status, **kwargs)  # noqa: E501

    @validate_arguments
    def health_get_with_http_info(self, check_id : Annotated[Optional[conlist(StrictStr)], Field(description="List of check_id (or check_id prefixes) that should be included in the response. If unset, health checks are not filtered by check_id. ")] = None, service_name : Annotated[Optional[conlist(StrictStr)], Field(description="List of service_name (or service_name prefixes) that should be included in the response. If unset, health checks are not filtered by service_name. ")] = None, status : Annotated[Optional[conlist(HealthStatus)], Field(description="List of status that should be included in the response. If unset, health checks are not filtered by status. ")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Appliance Health  # noqa: E501

        Report the appliance health along with the executed health checks. The health status is based on a set of health checks that are executed. Check the documentation of the individual health checks for more information.  Note that the status is only based on the health checks that are part of the response. If you filter out non-passing health checks, the top level status will be reported as passing.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.health_get_with_http_info(check_id, service_name, status, async_req=True)
        >>> result = thread.get()

        :param check_id: List of check_id (or check_id prefixes) that should be included in the response. If unset, health checks are not filtered by check_id. 
        :type check_id: List[str]
        :param service_name: List of service_name (or service_name prefixes) that should be included in the response. If unset, health checks are not filtered by service_name. 
        :type service_name: List[str]
        :param status: List of status that should be included in the response. If unset, health checks are not filtered by status. 
        :type status: List[HealthStatus]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(HealthGetResponseJson, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'check_id',
            'service_name',
            'status'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method health_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('check_id') is not None:  # noqa: E501
            _query_params.append(('check_id', _params['check_id']))
            _collection_formats['check_id'] = 'csv'

        if _params.get('service_name') is not None:  # noqa: E501
            _query_params.append(('service_name', _params['service_name']))
            _collection_formats['service_name'] = 'csv'

        if _params.get('status') is not None:  # noqa: E501
            _query_params.append(('status', _params['status']))
            _collection_formats['status'] = 'csv'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "HealthGetResponseJson",
        }

        return self.api_client.call_api(
            '/health', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
