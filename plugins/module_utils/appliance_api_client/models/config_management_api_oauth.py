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
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth_identity_provider import ConfigManagementApiOauthIdentityProvider
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth_role import ConfigManagementApiOauthRole
from ansible.module_utils.appliance_api_client.models.config_management_api_oauth_token_verification_key import ConfigManagementApiOauthTokenVerificationKey

class ConfigManagementApiOauth(BaseModel):
    """
    Open authorization (OAuth) configuration that can authorize users who want to access the Anapaya appliance management API.  # noqa: E501
    """
    enabled: Optional[StrictBool] = Field(False, description="Whether the feature is enabled.")
    identity_providers: Optional[conlist(ConfigManagementApiOauthIdentityProvider)] = Field(None, description="The identity providers. Currently only one is supported.")
    roles: Optional[conlist(ConfigManagementApiOauthRole)] = Field(None, description="Roles configuration used for OAuth.")
    token_verification_keys: Optional[conlist(ConfigManagementApiOauthTokenVerificationKey)] = Field(None, description="Keys to verify JWTs.")
    __properties = ["enabled", "identity_providers", "roles", "token_verification_keys"]

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
    def from_json(cls, json_str: str) -> ConfigManagementApiOauth:
        """Create an instance of ConfigManagementApiOauth from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in identity_providers (list)
        _items = []
        if self.identity_providers:
            for _item in self.identity_providers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identity_providers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in token_verification_keys (list)
        _items = []
        if self.token_verification_keys:
            for _item in self.token_verification_keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['token_verification_keys'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigManagementApiOauth:
        """Create an instance of ConfigManagementApiOauth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigManagementApiOauth.parse_obj(obj)

        _obj = ConfigManagementApiOauth.parse_obj({
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "identity_providers": [ConfigManagementApiOauthIdentityProvider.from_dict(_item) for _item in obj.get("identity_providers")] if obj.get("identity_providers") is not None else None,
            "roles": [ConfigManagementApiOauthRole.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "token_verification_keys": [ConfigManagementApiOauthTokenVerificationKey.from_dict(_item) for _item in obj.get("token_verification_keys")] if obj.get("token_verification_keys") is not None else None
        })
        return _obj


