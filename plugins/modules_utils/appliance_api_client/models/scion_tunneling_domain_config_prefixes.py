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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from openapi_client.models.scion_tunneling_prefixes_filter import ScionTunnelingPrefixesFilter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScionTunnelingDomainConfigPrefixes(BaseModel):
    """
    ScionTunnelingDomainConfigPrefixes
    """ # noqa: E501
    announce_filter: List[ScionTunnelingPrefixesFilter] = Field(description="A list of announced prefixes.")
    accept_filter: List[ScionTunnelingPrefixesFilter] = Field(description="A list of accepted prefixes.")
    __properties: ClassVar[List[str]] = ["announce_filter", "accept_filter"]

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
        """Create an instance of ScionTunnelingDomainConfigPrefixes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in announce_filter (list)
        _items = []
        if self.announce_filter:
            for _item in self.announce_filter:
                if _item:
                    _items.append(_item.to_dict())
            _dict['announce_filter'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in accept_filter (list)
        _items = []
        if self.accept_filter:
            for _item in self.accept_filter:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accept_filter'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScionTunnelingDomainConfigPrefixes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "announce_filter": [ScionTunnelingPrefixesFilter.from_dict(_item) for _item in obj.get("announce_filter")] if obj.get("announce_filter") is not None else None,
            "accept_filter": [ScionTunnelingPrefixesFilter.from_dict(_item) for _item in obj.get("accept_filter")] if obj.get("accept_filter") is not None else None
        })
        return _obj


