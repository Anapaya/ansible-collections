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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from openapi_client.models.config_system_ntp_servers import ConfigSystemNtpServers
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigSystemNtp(BaseModel):
    """
    Anapaya appliance NTP configuration.
    """ # noqa: E501
    root_distance_max: Optional[StrictStr] = Field(default='5s', description="Maximum acceptable root distance, i.e. the maximum estimated time required for a packet to travel to the server we are connected to from the server with the reference clock. If the current server does not satisfy this limit, the appliance will switch to a different server.")
    servers: Optional[List[ConfigSystemNtpServers]] = Field(default=None, description="List of NTP servers.")
    __properties: ClassVar[List[str]] = ["root_distance_max", "servers"]

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
        """Create an instance of ConfigSystemNtp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in servers (list)
        _items = []
        if self.servers:
            for _item in self.servers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['servers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigSystemNtp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "root_distance_max": obj.get("root_distance_max") if obj.get("root_distance_max") is not None else '5s',
            "servers": [ConfigSystemNtpServers.from_dict(_item) for _item in obj.get("servers")] if obj.get("servers") is not None else None
        })
        return _obj


