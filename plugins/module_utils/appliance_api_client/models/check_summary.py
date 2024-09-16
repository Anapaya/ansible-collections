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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from ansible.module_utils.appliance_api_client.models.status import Status

class CheckSummary(BaseModel):
    """
    CheckSummary
    """
    service: Optional[StrictStr] = Field(None, description="Name of the service.")
    name: StrictStr = Field(..., description="Name of health check.")
    status: Status = Field(...)
    data: Dict[str, Any] = Field(...)
    reason: Optional[StrictStr] = Field(None, description="Reason for check failure.")
    detail: Optional[StrictStr] = Field(None, description="Additional information.")
    __properties = ["service", "name", "status", "data", "reason", "detail"]

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
    def from_json(cls, json_str: str) -> CheckSummary:
        """Create an instance of CheckSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CheckSummary:
        """Create an instance of CheckSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CheckSummary.parse_obj(obj)

        _obj = CheckSummary.parse_obj({
            "service": obj.get("service"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "data": obj.get("data"),
            "reason": obj.get("reason"),
            "detail": obj.get("detail")
        })
        return _obj


