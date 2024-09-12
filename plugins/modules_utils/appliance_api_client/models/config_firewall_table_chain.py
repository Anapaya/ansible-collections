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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from openapi_client.models.config_firewall_table_chain_rule import ConfigFirewallTableChainRule
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigFirewallTableChain(BaseModel):
    """
    List of chains that are part of an nftables table, uniquely idenified by their name.
    """ # noqa: E501
    chaintype: Optional[StrictStr] = Field(default=None, description="The type and usage of the chain. This must be set for base chains and unset for regular chains.")
    hook: Optional[StrictStr] = Field(default=None, description="The packet processing step during which the chain should be executed. This must be set for base chains and unset for regular chains. For more information on the chain hooks, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains#Base_chain_hooks.")
    name: StrictStr = Field(description="The name of the chain.")
    policy: Optional[StrictStr] = Field(default=None, description="The default policy that will be applied to packets that reach the end of the chain. For more information on chain policies, please refer to https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains#Base_chain_policy.")
    priority: Optional[StrictInt] = Field(default=None, description="The priority of the chain. This must be set for base chains and unset for regular chains.")
    rules: Optional[List[ConfigFirewallTableChainRule]] = Field(default=None, description="Rules defined as part of a chain within a firewall table.")
    __properties: ClassVar[List[str]] = ["chaintype", "hook", "name", "policy", "priority", "rules"]

    @field_validator('chaintype')
    def chaintype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('FILTER', 'ROUTE', 'NAT'):
            raise ValueError("must be one of enum values ('FILTER', 'ROUTE', 'NAT')")
        return value

    @field_validator('hook')
    def hook_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PREROUTING', 'INPUT', 'FORWARD', 'OUTPUT', 'POSTROUTING'):
            raise ValueError("must be one of enum values ('PREROUTING', 'INPUT', 'FORWARD', 'OUTPUT', 'POSTROUTING')")
        return value

    @field_validator('policy')
    def policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACCEPT', 'DROP'):
            raise ValueError("must be one of enum values ('ACCEPT', 'DROP')")
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
        """Create an instance of ConfigFirewallTableChain from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigFirewallTableChain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chaintype": obj.get("chaintype"),
            "hook": obj.get("hook"),
            "name": obj.get("name"),
            "policy": obj.get("policy"),
            "priority": obj.get("priority"),
            "rules": [ConfigFirewallTableChainRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj


