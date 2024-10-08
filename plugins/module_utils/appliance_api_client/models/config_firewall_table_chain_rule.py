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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigFirewallTableChainRule(BaseModel):
    """
    List of firewall rules.
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="Description, or comment, for the firewall rule.")
    rule: StrictStr = Field(description="The rule definition consists of expressions and statements in string format. The expressions are evaluated from left to right and if the packet matches the expressions the statement is executed. For information on the supported syntax for expressions and statements, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Main_Page#Expressions:_Matching_packets and https://wiki.nftables.org/wiki-nftables/index.php/Main_Page#Statements:_Acting_on_packet_matches.")
    sequence_id: StrictInt = Field(description="The sequence ID determines the order in which sequence the firewall rules are applied. The sequence ID must be unique for each entry. Target devices apply the rules in order of ascending sequence ID (low to high).")
    __properties: ClassVar[List[str]] = ["comment", "rule", "sequence_id"]

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
        """Create an instance of ConfigFirewallTableChainRule from a JSON string"""
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
        """Create an instance of ConfigFirewallTableChainRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "rule": obj.get("rule"),
            "sequence_id": obj.get("sequence_id")
        })
        return _obj


