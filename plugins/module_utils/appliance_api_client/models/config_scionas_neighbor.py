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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from ansible.module_utils.appliance_api_client.models.config_scionas_neighbor_interface import ConfigSCIONASNeighborInterface
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigSCIONASNeighbor(BaseModel):
    """
    Neighbor SCION AS.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description, or comment, for the neighbor AS.")
    interfaces: Optional[List[ConfigSCIONASNeighborInterface]] = Field(default=None, description="SCION interfaces on this device that link to the neighbor AS.")
    neighbor_isd_as: StrictStr = Field(description="ISD-AS number of the neighbor AS.")
    relationship: StrictStr = Field(description="The relationship to the neighbor AS. If the local AS is core, this value must either be CORE or CHILD. If the local is non-core, this value must either be PARENT, CHILD or PEER.")
    __properties: ClassVar[List[str]] = ["description", "interfaces", "neighbor_isd_as", "relationship"]

    @field_validator('relationship')
    def relationship_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CORE', 'CHILD', 'PARENT', 'PEER'):
            raise ValueError("must be one of enum values ('CORE', 'CHILD', 'PARENT', 'PEER')")
        return value

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
        """Create an instance of ConfigSCIONASNeighbor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in interfaces (list)
        _items = []
        if self.interfaces:
            for _item in self.interfaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['interfaces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigSCIONASNeighbor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "interfaces": [ConfigSCIONASNeighborInterface.from_dict(_item) for _item in obj.get("interfaces")] if obj.get("interfaces") is not None else None,
            "neighbor_isd_as": obj.get("neighbor_isd_as"),
            "relationship": obj.get("relationship")
        })
        return _obj


