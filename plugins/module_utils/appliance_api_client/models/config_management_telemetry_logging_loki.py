# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: v0.37.1
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from ansible.module_utils.appliance_api_client.models.config_management_telemetry_logging_loki_basic_auth import ConfigManagementTelemetryLoggingLokiBasicAuth
from ansible.module_utils.appliance_api_client.models.config_management_telemetry_logging_loki_tls_config import ConfigManagementTelemetryLoggingLokiTlsConfig

class ConfigManagementTelemetryLoggingLoki(BaseModel):
    """
    Loki configuration.  # noqa: E501
    """
    basic_auth: Optional[ConfigManagementTelemetryLoggingLokiBasicAuth] = None
    tls_config: Optional[ConfigManagementTelemetryLoggingLokiTlsConfig] = None
    url: Optional[StrictStr] = Field(None, description="The url which is used to push logs to Loki.")
    __properties = ["basic_auth", "tls_config", "url"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConfigManagementTelemetryLoggingLoki:
        """Create an instance of ConfigManagementTelemetryLoggingLoki from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of basic_auth
        if self.basic_auth:
            _dict['basic_auth'] = self.basic_auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tls_config
        if self.tls_config:
            _dict['tls_config'] = self.tls_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigManagementTelemetryLoggingLoki:
        """Create an instance of ConfigManagementTelemetryLoggingLoki from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigManagementTelemetryLoggingLoki.parse_obj(obj)

        _obj = ConfigManagementTelemetryLoggingLoki.parse_obj({
            "basic_auth": ConfigManagementTelemetryLoggingLokiBasicAuth.from_dict(obj.get("basic_auth")) if obj.get("basic_auth") is not None else None,
            "tls_config": ConfigManagementTelemetryLoggingLokiTlsConfig.from_dict(obj.get("tls_config")) if obj.get("tls_config") is not None else None,
            "url": obj.get("url")
        })
        return _obj


