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
from pydantic import BaseModel, StrictInt
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigBgpNeighborTimers(BaseModel):
    """
    Timers related to a BGP neighbor
    """ # noqa: E501
    connect_retry: Optional[StrictInt] = Field(default=30, description="Time interval in seconds between attempts to establish a session with the peer.")
    hold_time: Optional[StrictInt] = Field(default=30, description="Time interval in seconds that a BGP session will be considered active in the absence of keepalive or other messages from the peer.    The hold-time is typically set to 3x the keepalive-interval.")
    keepalive_interval: Optional[StrictInt] = Field(default=10, description="Time interval in seconds between transmission of keepalive messages to the neighbor.    Typically set to 1/3 the hold-time.")
    minimum_advertisement_interval: Optional[StrictInt] = Field(default=30, description="Minimum time in seconds which must elapse between subsequent UPDATE messages relating to a common set of NLRI being transmitted to a peer. This timer is referred to as MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to reduce the number of UPDATE messages transmitted when a particular set of NLRI exhibit instability.")
    __properties: ClassVar[List[str]] = ["connect_retry", "hold_time", "keepalive_interval", "minimum_advertisement_interval"]

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
        """Create an instance of ConfigBgpNeighborTimers from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigBgpNeighborTimers from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connect_retry": obj.get("connect_retry") if obj.get("connect_retry") is not None else 30,
            "hold_time": obj.get("hold_time") if obj.get("hold_time") is not None else 30,
            "keepalive_interval": obj.get("keepalive_interval") if obj.get("keepalive_interval") is not None else 10,
            "minimum_advertisement_interval": obj.get("minimum_advertisement_interval") if obj.get("minimum_advertisement_interval") is not None else 30
        })
        return _obj


