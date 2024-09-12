# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: 0.1.0
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from openapi_client.models.tier_mapping import TierMapping
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FeatureMapping(BaseModel):
    """
    Describes for each product and tier what features are allowed. 
    """ # noqa: E501
    edge: Optional[TierMapping] = None
    core: Optional[TierMapping] = None
    gate: Optional[TierMapping] = None
    other: Optional[TierMapping] = None
    __properties: ClassVar[List[str]] = ["edge", "core", "gate", "other"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FeatureMapping from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of edge
        if self.edge:
            _dict['edge'] = self.edge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of core
        if self.core:
            _dict['core'] = self.core.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gate
        if self.gate:
            _dict['gate'] = self.gate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of other
        if self.other:
            _dict['other'] = self.other.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FeatureMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edge": TierMapping.from_dict(obj.get("edge")) if obj.get("edge") is not None else None,
            "core": TierMapping.from_dict(obj.get("core")) if obj.get("core") is not None else None,
            "gate": TierMapping.from_dict(obj.get("gate")) if obj.get("gate") is not None else None,
            "other": TierMapping.from_dict(obj.get("other")) if obj.get("other") is not None else None
        })
        return _obj


