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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_endpoint_allowed_interfaces import ConfigScionTunnelingEndpointAllowedInterfaces

class ConfigScionTunnelingEndpoint(BaseModel):
    """
    Local IP-in-SCION tunnel endpoint configuration  # noqa: E501
    """
    allowed_interfaces: Optional[conlist(ConfigScionTunnelingEndpointAllowedInterfaces)] = Field(None, description="The SCION interfaces for each local SCION AS that are allowed to be used by this IP-in-SCION tunneling endpoint. This can be used to control incoming traffic, e.g., if a tunnel endpoint should only be reachable via SCION interfaces 1 and 2, allowed-interfaces should list them explicitly. Remote tunnel endpoints will then only choose paths entering the respective local AS via SCION interface 1 or 2. If the IP-in-SCION tunneling endpoint on this appliance should be reachable via a SCION interface of a peer appliance, the allowed-interfaces list must be configured with the respective SCION interface of the peer appliance. By default the list is empty, in this case the appliance will automatically configure the locally configured SCION interfaces as allowed-interfaces. Automatic configuration is disabled if topology synchronization is enabled or if disable_auto_allowed_interfaces is set.")
    control_port: Optional[StrictInt] = Field(None, description="Port number for control traffic. The control address is constructed from the ip address and this control port. The control address is used to exchange IP routing information as part of SGRP. If not set, or zero, the control port will be dynamically allocated.")
    data_port: Optional[StrictInt] = Field(None, description="Port number for data traffic. The data address is constructed from the ip address and this control port. The data address is used for the IP-in-SCION encapsulated traffic stream. If not set, or zero, the data port will be dynamically allocated.")
    description: Optional[StrictStr] = Field(None, description="Optional description of the IP-in-SCION tunnel endpoint.")
    disable_auto_allowed_interfaces: Optional[StrictBool] = Field(None, description="Whether the automatic configuration of allowed interfaces should be disabled. When disabled, the IP-in-SCION tunneling endpoint will be reached by remote endpoints on all SCION interfaces of the locally configured AS. When enabled (default), the local IP-in-SCION tunneling endpoint will only be reached by remote endpoints on the SCION interfaces that are configured on the local appliance.")
    disable_urpf: Optional[StrictBool] = Field(None, description="Flag to disable uRPF. When enabled (default), the gateway performs strict URPF for all the received IP-in-SCION-tunneled traffic, checking that incoming IP packets have a source address that is within the announced prefixes by a remote gateway, and that the SCION packets are sent from a valid remote ISD-AS and are encrypted as configured in the associated domain.")
    enable_scion_rss: Optional[StrictBool] = Field(None, description="Flag to activate SCION RSS. If activated, the gateway utilizes UDP source port entropy on the underlay such that sibling routers can leverage RSS for SCION traffic. This can greatly improve throughput performance. This must only be set to true if the routers supports SCION RSS.")
    enabled: Optional[StrictBool] = Field(None, description="Whether this endpoint is enabled.")
    ip: Optional[StrictStr] = Field(None, description="IP address of the local IP-in-SCION endpoint.")
    probe_port: Optional[StrictInt] = Field(None, description="Port number for probing traffic. The probe address is constructed from the ip address and this probe port. The probe address is used by remote tunnel endpoints in their health probing. If not set, or zero, the probe port will be dynamically allocated.")
    __properties = ["allowed_interfaces", "control_port", "data_port", "description", "disable_auto_allowed_interfaces", "disable_urpf", "enable_scion_rss", "enabled", "ip", "probe_port"]

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
    def from_json(cls, json_str: str) -> ConfigScionTunnelingEndpoint:
        """Create an instance of ConfigScionTunnelingEndpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_interfaces (list)
        _items = []
        if self.allowed_interfaces:
            for _item in self.allowed_interfaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allowed_interfaces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigScionTunnelingEndpoint:
        """Create an instance of ConfigScionTunnelingEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigScionTunnelingEndpoint.parse_obj(obj)

        _obj = ConfigScionTunnelingEndpoint.parse_obj({
            "allowed_interfaces": [ConfigScionTunnelingEndpointAllowedInterfaces.from_dict(_item) for _item in obj.get("allowed_interfaces")] if obj.get("allowed_interfaces") is not None else None,
            "control_port": obj.get("control_port"),
            "data_port": obj.get("data_port"),
            "description": obj.get("description"),
            "disable_auto_allowed_interfaces": obj.get("disable_auto_allowed_interfaces"),
            "disable_urpf": obj.get("disable_urpf"),
            "enable_scion_rss": obj.get("enable_scion_rss"),
            "enabled": obj.get("enabled"),
            "ip": obj.get("ip"),
            "probe_port": obj.get("probe_port")
        })
        return _obj


