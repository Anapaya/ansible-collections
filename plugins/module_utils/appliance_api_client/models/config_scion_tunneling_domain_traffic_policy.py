# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: v0.37.1
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_traffic_policy_failover_sequence_entry import ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry

class ConfigScionTunnelingDomainTrafficPolicy(BaseModel):
    """
    List of traffic policies.  # noqa: E501
    """
    description: Optional[StrictStr] = Field(None, description="The optional description of the traffic policy.")
    failover_sequence: Optional[conlist(ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry)] = Field(None, description="A list of failover sequence entries, each of them associated with a path filter. If there's no live path left after applying the first filter the second one is tried and so on.")
    sequence_id: StrictInt = Field(..., description="The sequence ID determines the order in which sequence the traffic policies are applied. The sequence ID must be unique for each entry. Target devices try to find the first entry with a matching traffic matcher in ascending order determined by the sequence ID (low to high).")
    traffic_matcher: StrictStr = Field(..., description="Reference of the traffic matcher that is utilized by this policy. The traffic matcher is a selector for the IP packets covered by this traffic policy.")
    __properties = ["description", "failover_sequence", "sequence_id", "traffic_matcher"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConfigScionTunnelingDomainTrafficPolicy:
        """Create an instance of ConfigScionTunnelingDomainTrafficPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in failover_sequence (list)
        _items = []
        if self.failover_sequence:
            for _item in self.failover_sequence:
                if _item:
                    _items.append(_item.to_dict())
            _dict['failover_sequence'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigScionTunnelingDomainTrafficPolicy:
        """Create an instance of ConfigScionTunnelingDomainTrafficPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigScionTunnelingDomainTrafficPolicy.parse_obj(obj)

        _obj = ConfigScionTunnelingDomainTrafficPolicy.parse_obj({
            "description": obj.get("description"),
            "failover_sequence": [ConfigScionTunnelingDomainTrafficPolicyFailoverSequenceEntry.from_dict(_item) for _item in obj.get("failover_sequence")] if obj.get("failover_sequence") is not None else None,
            "sequence_id": obj.get("sequence_id"),
            "traffic_matcher": obj.get("traffic_matcher")
        })
        return _obj


