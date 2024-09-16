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



from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, validator
from ansible.module_utils.appliance_api_client.models.link_relationship import LinkRelationship

class DebugScionSiblingInterface(BaseModel):
    """
    DebugScionSiblingInterface
    """
    mtu: StrictInt = Field(..., description="The MTU of the SCION interface")
    relationship: LinkRelationship = Field(...)
    remote_isd_as: constr(strict=True) = Field(...)
    local_isd_as: constr(strict=True) = Field(...)
    local_interface_id: StrictInt = Field(..., description="The ID of the Interface.")
    next_hop_address: StrictStr = Field(..., description="The IP and port of the next hop.")
    __properties = ["mtu", "relationship", "remote_isd_as", "local_isd_as", "local_interface_id", "next_hop_address"]

    @validator('remote_isd_as')
    def remote_isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
        return value

    @validator('local_isd_as')
    def local_isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
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
    def from_json(cls, json_str: str) -> DebugScionSiblingInterface:
        """Create an instance of DebugScionSiblingInterface from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DebugScionSiblingInterface:
        """Create an instance of DebugScionSiblingInterface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DebugScionSiblingInterface.parse_obj(obj)

        _obj = DebugScionSiblingInterface.parse_obj({
            "mtu": obj.get("mtu"),
            "relationship": obj.get("relationship"),
            "remote_isd_as": obj.get("remote_isd_as"),
            "local_isd_as": obj.get("local_isd_as"),
            "local_interface_id": obj.get("local_interface_id"),
            "next_hop_address": obj.get("next_hop_address")
        })
        return _obj


