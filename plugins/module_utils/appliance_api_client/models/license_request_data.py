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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from ansible.module_utils.appliance_api_client.models.appliance_description import ApplianceDescription

class LicenseRequestData(BaseModel):
    """
    LicenseRequestData
    """
    appliance_id: StrictStr = Field(..., description="The appliance ID for which the license is requested.")
    scion_activation_date: Optional[datetime] = Field(None, description="The date and time when SCION was first activated on the appliance.")
    appliance_version: StrictStr = Field(..., description="The version of the appliance for which the license is requested.")
    appliance_description: ApplianceDescription = Field(...)
    __properties = ["appliance_id", "scion_activation_date", "appliance_version", "appliance_description"]

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
    def from_json(cls, json_str: str) -> LicenseRequestData:
        """Create an instance of LicenseRequestData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of appliance_description
        if self.appliance_description:
            _dict['appliance_description'] = self.appliance_description.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LicenseRequestData:
        """Create an instance of LicenseRequestData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LicenseRequestData.parse_obj(obj)

        _obj = LicenseRequestData.parse_obj({
            "appliance_id": obj.get("appliance_id"),
            "scion_activation_date": obj.get("scion_activation_date"),
            "appliance_version": obj.get("appliance_version"),
            "appliance_description": ApplianceDescription.from_dict(obj.get("appliance_description")) if obj.get("appliance_description") is not None else None
        })
        return _obj


