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
from pydantic import BaseModel, Field, conlist
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain import ConfigScionTunnelingDomain
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_endpoint import ConfigScionTunnelingEndpoint
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_path_filter import ConfigScionTunnelingPathFilter
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_remote import ConfigScionTunnelingRemote
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_static_announcement import ConfigScionTunnelingStaticAnnouncement
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_traffic_matcher import ConfigScionTunnelingTrafficMatcher

class ConfigScionTunneling(BaseModel):
    """
    Top-level configuration and state for IP-in-SCION tunneling.  # noqa: E501
    """
    domains: Optional[conlist(ConfigScionTunnelingDomain)] = Field(None, description="List of domains that define the rules by which IP packets are routed. A domain is a subset of the IP space that shares the same policies.")
    endpoint: Optional[ConfigScionTunnelingEndpoint] = None
    path_filters: Optional[conlist(ConfigScionTunnelingPathFilter)] = Field(None, description="List of path filters that can be referenced by name from a path policies. A path filter defines a set of paths by applying the filter to all available paths.")
    remotes: Optional[conlist(ConfigScionTunnelingRemote)] = Field(None, description="List of remote ISD-ASes that are connected with the gateway. The remote ISD-ASes can be referenced in the remote matchers of the domains.")
    static_announcements: Optional[conlist(ConfigScionTunnelingStaticAnnouncement)] = Field(None, description="List of static routes that are advertised. The routes are only advertised to the domains with matching announce filters.")
    traffic_matchers: Optional[conlist(ConfigScionTunnelingTrafficMatcher)] = Field(None, description="List of traffic matchers that can be referenced by name from a traffic policy. A matcher is used to classify traffic for tunneling. Each packet is classified based on configured traffic matchers and put in a traffic class. A traffic class is used in a traffic policy to map a path policy to a traffic class.")
    __properties = ["domains", "endpoint", "path_filters", "remotes", "static_announcements", "traffic_matchers"]

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
    def from_json(cls, json_str: str) -> ConfigScionTunneling:
        """Create an instance of ConfigScionTunneling from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in domains (list)
        _items = []
        if self.domains:
            for _item in self.domains:
                if _item:
                    _items.append(_item.to_dict())
            _dict['domains'] = _items
        # override the default output from pydantic by calling `to_dict()` of endpoint
        if self.endpoint:
            _dict['endpoint'] = self.endpoint.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in path_filters (list)
        _items = []
        if self.path_filters:
            for _item in self.path_filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['path_filters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in remotes (list)
        _items = []
        if self.remotes:
            for _item in self.remotes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['remotes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in static_announcements (list)
        _items = []
        if self.static_announcements:
            for _item in self.static_announcements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['static_announcements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in traffic_matchers (list)
        _items = []
        if self.traffic_matchers:
            for _item in self.traffic_matchers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['traffic_matchers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigScionTunneling:
        """Create an instance of ConfigScionTunneling from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigScionTunneling.parse_obj(obj)

        _obj = ConfigScionTunneling.parse_obj({
            "domains": [ConfigScionTunnelingDomain.from_dict(_item) for _item in obj.get("domains")] if obj.get("domains") is not None else None,
            "endpoint": ConfigScionTunnelingEndpoint.from_dict(obj.get("endpoint")) if obj.get("endpoint") is not None else None,
            "path_filters": [ConfigScionTunnelingPathFilter.from_dict(_item) for _item in obj.get("path_filters")] if obj.get("path_filters") is not None else None,
            "remotes": [ConfigScionTunnelingRemote.from_dict(_item) for _item in obj.get("remotes")] if obj.get("remotes") is not None else None,
            "static_announcements": [ConfigScionTunnelingStaticAnnouncement.from_dict(_item) for _item in obj.get("static_announcements")] if obj.get("static_announcements") is not None else None,
            "traffic_matchers": [ConfigScionTunnelingTrafficMatcher.from_dict(_item) for _item in obj.get("traffic_matchers")] if obj.get("traffic_matchers") is not None else None
        })
        return _obj


