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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from ansible.module_utils.appliance_api_client.models.config_management_api_basic_auth import ConfigManagementApiBasicAuth
from ansible.module_utils.appliance_api_client.models.config_management_api_listener import ConfigManagementApiListener
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth import ConfigManagementApiOauth

class ConfigManagementApi(BaseModel):
    """
    Anapaya appliance management API configuration.  # noqa: E501
    """
    basic_auth: Optional[ConfigManagementApiBasicAuth] = None
    listeners: Optional[conlist(ConfigManagementApiListener)] = Field(None, description="List of management API listeners that define where the API is exposed")
    oauth: Optional[ConfigManagementApiOauth] = None
    unprotected: Optional[StrictBool] = Field(False, description="Whether the management API is allowed to be exposed without authentication. Always make sure to properly protect your API.")
    __properties = ["basic_auth", "listeners", "oauth", "unprotected"]

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
    def from_json(cls, json_str: str) -> ConfigManagementApi:
        """Create an instance of ConfigManagementApi from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in listeners (list)
        _items = []
        if self.listeners:
            for _item in self.listeners:
                if _item:
                    _items.append(_item.to_dict())
            _dict['listeners'] = _items
        # override the default output from pydantic by calling `to_dict()` of oauth
        if self.oauth:
            _dict['oauth'] = self.oauth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigManagementApi:
        """Create an instance of ConfigManagementApi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigManagementApi.parse_obj(obj)

        _obj = ConfigManagementApi.parse_obj({
            "basic_auth": ConfigManagementApiBasicAuth.from_dict(obj.get("basic_auth")) if obj.get("basic_auth") is not None else None,
            "listeners": [ConfigManagementApiListener.from_dict(_item) for _item in obj.get("listeners")] if obj.get("listeners") is not None else None,
            "oauth": ConfigManagementApiOauth.from_dict(obj.get("oauth")) if obj.get("oauth") is not None else None,
            "unprotected": obj.get("unprotected") if obj.get("unprotected") is not None else False
        })
        return _obj


