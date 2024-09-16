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
from ansible.module_utils.appliance_api_client.models.bgp_neighbor import BGPNeighbor

class BGPConfig(BaseModel):
    """
    BGP configuration the host.  # noqa: E501
    """
    asn: StrictInt = Field(..., description="The local AS number used for the BGP sessions.")
    router_id: StrictStr = Field(..., description="The router ID used for the BGP sessions.")
    neighbors: conlist(BGPNeighbor) = Field(..., description="The BGP neighbors.")
    networks: conlist(StrictStr) = Field(..., description="The prefixes in CIDR format that are advertised in the BGP sessions.")
    __properties = ["asn", "router_id", "neighbors", "networks"]

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
    def from_json(cls, json_str: str) -> BGPConfig:
        """Create an instance of BGPConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in neighbors (list)
        _items = []
        if self.neighbors:
            for _item in self.neighbors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['neighbors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BGPConfig:
        """Create an instance of BGPConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BGPConfig.parse_obj(obj)

        _obj = BGPConfig.parse_obj({
            "asn": obj.get("asn"),
            "router_id": obj.get("router_id"),
            "neighbors": [BGPNeighbor.from_dict(_item) for _item in obj.get("neighbors")] if obj.get("neighbors") is not None else None,
            "networks": obj.get("networks")
        })
        return _obj


