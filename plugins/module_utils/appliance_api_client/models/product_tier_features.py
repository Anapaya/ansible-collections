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
from pydantic import BaseModel
from ansible.module_utils.appliance_api_client.models.lan_features import LANFeatures
from ansible.module_utils.appliance_api_client.models.management_features import ManagementFeatures
from ansible.module_utils.appliance_api_client.models.scion_features import SCIONFeatures
from ansible.module_utils.appliance_api_client.models.tunneling_features import TunnelingFeatures

class ProductTierFeatures(BaseModel):
    """
    Describes the features that are allowed.   # noqa: E501
    """
    management: Optional[ManagementFeatures] = None
    scion_tunneling: Optional[TunnelingFeatures] = None
    scion: Optional[SCIONFeatures] = None
    lan: Optional[LANFeatures] = None
    __properties = ["management", "scion_tunneling", "scion", "lan"]

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
    def from_json(cls, json_str: str) -> ProductTierFeatures:
        """Create an instance of ProductTierFeatures from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of management
        if self.management:
            _dict['management'] = self.management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scion_tunneling
        if self.scion_tunneling:
            _dict['scion_tunneling'] = self.scion_tunneling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scion
        if self.scion:
            _dict['scion'] = self.scion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lan
        if self.lan:
            _dict['lan'] = self.lan.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductTierFeatures:
        """Create an instance of ProductTierFeatures from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductTierFeatures.parse_obj(obj)

        _obj = ProductTierFeatures.parse_obj({
            "management": ManagementFeatures.from_dict(obj.get("management")) if obj.get("management") is not None else None,
            "scion_tunneling": TunnelingFeatures.from_dict(obj.get("scion_tunneling")) if obj.get("scion_tunneling") is not None else None,
            "scion": SCIONFeatures.from_dict(obj.get("scion")) if obj.get("scion") is not None else None,
            "lan": LANFeatures.from_dict(obj.get("lan")) if obj.get("lan") is not None else None
        })
        return _obj


