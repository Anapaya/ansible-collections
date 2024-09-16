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
from pydantic import Field, StrictStr
from ansible.module_utils.appliance_api_client.models.error_base import ErrorBase

class BasicError(ErrorBase):
    """
    BasicError
    """
    detail: Optional[StrictStr] = Field(None, description="A human readable explanation specific to this occurrence of the problem that is helpful to locate the problem and give advice on how to proceed. Written in English and readable for engineers, usually not suited for non technical stakeholders and not localized.")
    __properties = ["type", "title", "status", "detail"]

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
    def from_json(cls, json_str: str) -> BasicError:
        """Create an instance of BasicError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BasicError:
        """Create an instance of BasicError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BasicError.parse_obj(obj)

        _obj = BasicError.parse_obj({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "status": obj.get("status"),
            "detail": obj.get("detail")
        })
        return _obj


