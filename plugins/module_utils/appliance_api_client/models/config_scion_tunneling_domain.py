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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_prefixes import ConfigScionTunnelingDomainPrefixes
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_remote_matcher import ConfigScionTunnelingDomainRemoteMatcher
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_traffic_policy import ConfigScionTunnelingDomainTrafficPolicy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigScionTunnelingDomain(BaseModel):
    """
    List of domains.
    """ # noqa: E501
    default: Optional[StrictBool] = Field(default=None, description="Whether this domain is the default domain. The default domain is assumed to accept the whole IP space that is not covered by other domains. Because of this it may not specify an accept-filter.")
    description: Optional[StrictStr] = Field(default=None, description="Optional description, or comment, for the domain.")
    local_isd_ases: Optional[List[StrictStr]] = Field(default=None, description="List of local ISD-AS identifiers that belong to this domain. Traffic towards remote ISD-ASes is guaranteed to only use paths that start at one of these local ISD-ASes.")
    name: StrictStr = Field(description="The name of the domain.")
    prefixes: Optional[ConfigScionTunnelingDomainPrefixes] = None
    remote_isd_ases: Optional[List[ConfigScionTunnelingDomainRemoteMatcher]] = Field(default=None, description="List of remote ISD-AS identifiers that belong to this domain. Prefix announcements will be accepted from these remote ISD-ASes. All IP traffic will be tunneled over paths that end in one of these remote ISD-ASes.")
    traffic_policies: Optional[List[ConfigScionTunnelingDomainTrafficPolicy]] = Field(default=None, description="List of traffic policies that configure the types of traffic that are tunneled via this domain and the tunnel properties. A traffic policy defines a matcher on the IP traffic (the traffic matcher). If the IP traffic matches, it is tunneled to the remote SCION AS. Acceptable paths for the tunnel are defined via the path policy")
    __properties: ClassVar[List[str]] = ["default", "description", "local_isd_ases", "name", "prefixes", "remote_isd_ases", "traffic_policies"]

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
        """Create an instance of ConfigScionTunnelingDomain from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of prefixes
        if self.prefixes:
            _dict['prefixes'] = self.prefixes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in remote_isd_ases (list)
        _items = []
        if self.remote_isd_ases:
            for _item in self.remote_isd_ases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['remote_isd_ases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in traffic_policies (list)
        _items = []
        if self.traffic_policies:
            for _item in self.traffic_policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['traffic_policies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigScionTunnelingDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "default": obj.get("default"),
            "description": obj.get("description"),
            "local_isd_ases": obj.get("local_isd_ases"),
            "name": obj.get("name"),
            "prefixes": ConfigScionTunnelingDomainPrefixes.from_dict(obj.get("prefixes")) if obj.get("prefixes") is not None else None,
            "remote_isd_ases": [ConfigScionTunnelingDomainRemoteMatcher.from_dict(_item) for _item in obj.get("remote_isd_ases")] if obj.get("remote_isd_ases") is not None else None,
            "traffic_policies": [ConfigScionTunnelingDomainTrafficPolicy.from_dict(_item) for _item in obj.get("traffic_policies")] if obj.get("traffic_policies") is not None else None
        })
        return _obj


