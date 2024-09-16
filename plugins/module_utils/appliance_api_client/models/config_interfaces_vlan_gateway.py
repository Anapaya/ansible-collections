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

class ConfigInterfacesVlanGateway(BaseModel):
    """
    The gateway for the network interface.  # noqa: E501
    """
    ipv4_gateway: Optional[StrictStr] = Field(None, description="The gateway address for the IPv4 networking stack. Note that there must only be one IPv4 gateway configured across all the interfaces.")
    ipv6_gateway: Optional[StrictStr] = Field(None, description="The gateway address for the IPv6 networking stack. Note that there must only be one IPv6 gateway configured across all the interfaces.")
    __properties = ["ipv4_gateway", "ipv6_gateway"]

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
    def from_json(cls, json_str: str) -> ConfigInterfacesVlanGateway:
        """Create an instance of ConfigInterfacesVlanGateway from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigInterfacesVlanGateway:
        """Create an instance of ConfigInterfacesVlanGateway from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigInterfacesVlanGateway.parse_obj(obj)

        _obj = ConfigInterfacesVlanGateway.parse_obj({
            "ipv4_gateway": obj.get("ipv4_gateway"),
            "ipv6_gateway": obj.get("ipv6_gateway")
        })
        return _obj


