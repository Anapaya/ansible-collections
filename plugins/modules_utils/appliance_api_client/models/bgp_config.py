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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.bgp_neighbor import BGPNeighbor
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BGPConfig(BaseModel):
    """
    BGP configuration the host.
    """ # noqa: E501
    asn: StrictInt = Field(description="The local AS number used for the BGP sessions.")
    router_id: StrictStr = Field(description="The router ID used for the BGP sessions.")
    neighbors: List[BGPNeighbor] = Field(description="The BGP neighbors.")
    networks: List[StrictStr] = Field(description="The prefixes in CIDR format that are advertised in the BGP sessions.")
    __properties: ClassVar[List[str]] = ["asn", "router_id", "neighbors", "networks"]

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
        """Create an instance of BGPConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in neighbors (list)
        _items = []
        if self.neighbors:
            for _item in self.neighbors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['neighbors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BGPConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asn": obj.get("asn"),
            "router_id": obj.get("router_id"),
            "neighbors": [BGPNeighbor.from_dict(_item) for _item in obj.get("neighbors")] if obj.get("neighbors") is not None else None,
            "networks": obj.get("networks")
        })
        return _obj


