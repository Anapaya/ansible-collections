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

class ConfigManagementApiOauthTokenVerificationKey(BaseModel):
    """
    The list of JWT verification keys specified as a JSON Web Key Set (JWKS).  Each key set contains keys that enable the appliance to verify tokens signed by corresponding private keys. This is useful in case the appliance API is not accessed via a browser where the OAuth redirect flow of the identity provider likely does not work. This list is not required if the browser redirect flow is enough for your use case.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="The identifier of the key. Must be unique among all keys.")
    jwks_url: Optional[StrictStr] = Field(None, description="URL for fetching JSON Web Key Sets.")
    __properties = ["id", "jwks_url"]

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
    def from_json(cls, json_str: str) -> ConfigManagementApiOauthTokenVerificationKey:
        """Create an instance of ConfigManagementApiOauthTokenVerificationKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigManagementApiOauthTokenVerificationKey:
        """Create an instance of ConfigManagementApiOauthTokenVerificationKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigManagementApiOauthTokenVerificationKey.parse_obj(obj)

        _obj = ConfigManagementApiOauthTokenVerificationKey.parse_obj({
            "id": obj.get("id"),
            "jwks_url": obj.get("jwks_url")
        })
        return _obj


