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



from pydantic import BaseModel, Field
from ansible.module_utils.appliance_api_client.models.ping_summary import PingSummary

class ToolsScionPingPostResponseJson(BaseModel):
    """
    ToolsScionPingPostResponseJson
    """
    summary: PingSummary = Field(...)
    __properties = ["summary"]

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
    def from_json(cls, json_str: str) -> ToolsScionPingPostResponseJson:
        """Create an instance of ToolsScionPingPostResponseJson from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ToolsScionPingPostResponseJson:
        """Create an instance of ToolsScionPingPostResponseJson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ToolsScionPingPostResponseJson.parse_obj(obj)

        _obj = ToolsScionPingPostResponseJson.parse_obj({
            "summary": PingSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None
        })
        return _obj


