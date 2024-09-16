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
from ansible.module_utils.appliance_api_client.models.scion_tunneling_failover_sequence_entry import ScionTunnelingFailoverSequenceEntry
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScionTunnelingTrafficMatcher(BaseModel):
    """
    ScionTunnelingTrafficMatcher
    """ # noqa: E501
    traffic_policy_id: StrictInt = Field(description="Unique ID of this traffic class.")
    traffic_matcher: StrictStr = Field(description="Name of the corresponding traffic matcher.")
    failover_sequence: List[ScionTunnelingFailoverSequenceEntry] = Field(description="A failover sequence. If there are no healthy sessions in the first entry, the second one is used and so on. ")
    selected_session: StrictStr = Field(description="The ID of the session currently used to handle this traffic class.")
    selected_session_legacy: StrictInt = Field(description="The ID of the session currently used to handle this traffic class.")
    selected_path: StrictStr = Field(description="The SCION path currently used to handle this traffic class.")
    __properties: ClassVar[List[str]] = ["traffic_policy_id", "traffic_matcher", "failover_sequence", "selected_session", "selected_session_legacy", "selected_path"]

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
        """Create an instance of ScionTunnelingTrafficMatcher from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failover_sequence (list)
        _items = []
        if self.failover_sequence:
            for _item in self.failover_sequence:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failover_sequence'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScionTunnelingTrafficMatcher from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "traffic_policy_id": obj.get("traffic_policy_id"),
            "traffic_matcher": obj.get("traffic_matcher"),
            "failover_sequence": [ScionTunnelingFailoverSequenceEntry.from_dict(_item) for _item in obj.get("failover_sequence")] if obj.get("failover_sequence") is not None else None,
            "selected_session": obj.get("selected_session"),
            "selected_session_legacy": obj.get("selected_session_legacy"),
            "selected_path": obj.get("selected_path")
        })
        return _obj


