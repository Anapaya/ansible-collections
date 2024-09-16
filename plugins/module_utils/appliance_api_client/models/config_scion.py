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


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from ansible.module_utils.appliance_api_client.models.config_scion_synchronization import ConfigSCIONSynchronization
from ansible.module_utils.appliance_api_client.models.config_scionas import ConfigSCIONAS

class ConfigSCION(BaseModel):
    """
    Top-level configuration and state for the SCION protocol.  # noqa: E501
    """
    ases: Optional[conlist(ConfigSCIONAS)] = Field(None, description="List of SCION ASes that this device is part of identified by their ISD-AS identifier.")
    synchronization: Optional[ConfigSCIONSynchronization] = None
    __properties = ["ases", "synchronization"]

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
    def from_json(cls, json_str: str) -> ConfigSCION:
        """Create an instance of ConfigSCION from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in ases (list)
        _items = []
        if self.ases:
            for _item in self.ases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ases'] = _items
        # override the default output from pydantic by calling `to_dict()` of synchronization
        if self.synchronization:
            _dict['synchronization'] = self.synchronization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigSCION:
        """Create an instance of ConfigSCION from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigSCION.parse_obj(obj)

        _obj = ConfigSCION.parse_obj({
            "ases": [ConfigSCIONAS.from_dict(_item) for _item in obj.get("ases")] if obj.get("ases") is not None else None,
            "synchronization": ConfigSCIONSynchronization.from_dict(obj.get("synchronization")) if obj.get("synchronization") is not None else None
        })
        return _obj


