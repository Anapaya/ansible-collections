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



from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class TRCForLocalISDAvailableNotFound(BaseModel):
    """
    TRCForLocalISDAvailableNotFound
    """
    isd: StrictInt = Field(..., description="The ISD of the TRC.")
    data_type: StrictStr = Field(...)
    __properties = ["isd", "data_type"]

    @validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('not_found'):
            raise ValueError("must be one of enum values ('not_found')")
        return value

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
    def from_json(cls, json_str: str) -> TRCForLocalISDAvailableNotFound:
        """Create an instance of TRCForLocalISDAvailableNotFound from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TRCForLocalISDAvailableNotFound:
        """Create an instance of TRCForLocalISDAvailableNotFound from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TRCForLocalISDAvailableNotFound.parse_obj(obj)

        _obj = TRCForLocalISDAvailableNotFound.parse_obj({
            "isd": obj.get("isd"),
            "data_type": obj.get("data_type")
        })
        return _obj


