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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_static_announcement_next_hop_tracking import ConfigScionTunnelingStaticAnnouncementNextHopTracking
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigScionTunnelingStaticAnnouncement(BaseModel):
    """
    List of static announcements.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description, or comment, for the target.")
    next_hop_tracking: Optional[ConfigScionTunnelingStaticAnnouncementNextHopTracking] = None
    prefixes: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="The IP prefixes that are statically configured and advertised via SGRP")
    sequence_id: StrictInt = Field(description="The sequence ID defines the order of the static route entries. The sequence ID must be unique for each entry.")
    __properties: ClassVar[List[str]] = ["description", "next_hop_tracking", "prefixes", "sequence_id"]

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
        """Create an instance of ConfigScionTunnelingStaticAnnouncement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of next_hop_tracking
        if self.next_hop_tracking:
            _dict['next_hop_tracking'] = self.next_hop_tracking.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigScionTunnelingStaticAnnouncement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "next_hop_tracking": ConfigScionTunnelingStaticAnnouncementNextHopTracking.from_dict(obj.get("next_hop_tracking")) if obj.get("next_hop_tracking") is not None else None,
            "prefixes": obj.get("prefixes"),
            "sequence_id": obj.get("sequence_id")
        })
        return _obj


