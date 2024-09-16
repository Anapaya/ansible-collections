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


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class AcceptFilterMatchesPrefixData(BaseModel):
    """
    The entry in the accept filter matches at least one prefix that is received from remotes in the domain. While it is not invalid to have an accept filter entry that does not match anything, it is certainly curious. This health check is meant to help operators identify such cases. This only applies to the entries with action `accept`.  If `count` is zero, the status is `notice`. Otherwise, the status is `passing`.   # noqa: E501
    """
    domain: StrictStr = Field(..., description="The domain the accept filter entry is part of. ")
    prefixes: conlist(StrictStr) = Field(..., description="The prefixes that the filter entry is configured with. This is not the set of prefixes that are actually matched by the entry. ")
    count: StrictInt = Field(..., description="The number of prefixes that are matched by the accept filter entry. We count unique prefixes, so if a prefix is matched multiple times, or is announced by multiple remotes, it only counts once. Two overlapping prefixes are counted individually. ")
    __properties = ["domain", "prefixes", "count"]

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
    def from_json(cls, json_str: str) -> AcceptFilterMatchesPrefixData:
        """Create an instance of AcceptFilterMatchesPrefixData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AcceptFilterMatchesPrefixData:
        """Create an instance of AcceptFilterMatchesPrefixData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AcceptFilterMatchesPrefixData.parse_obj(obj)

        _obj = AcceptFilterMatchesPrefixData.parse_obj({
            "domain": obj.get("domain"),
            "prefixes": obj.get("prefixes"),
            "count": obj.get("count")
        })
        return _obj


