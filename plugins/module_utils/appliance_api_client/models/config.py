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


from typing import Optional
from pydantic import BaseModel
from ansible.module_utils.appliance_api_client.models.config_advanced import ConfigAdvanced
from ansible.module_utils.appliance_api_client.models.config_bgp import ConfigBgp
from ansible.module_utils.appliance_api_client.models.config_cluster import ConfigCluster
from ansible.module_utils.appliance_api_client.models.config_experiments import ConfigExperiments
from ansible.module_utils.appliance_api_client.models.config_firewall import ConfigFirewall
from ansible.module_utils.appliance_api_client.models.config_interfaces import ConfigInterfaces
from ansible.module_utils.appliance_api_client.models.config_management import ConfigManagement
from ansible.module_utils.appliance_api_client.models.config_nat import ConfigNat
from ansible.module_utils.appliance_api_client.models.config_scion import ConfigSCION
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling import ConfigScionTunneling
from ansible.module_utils.appliance_api_client.models.config_system import ConfigSystem

class Config(BaseModel):
    """
    Anapaya appliance configuration  # noqa: E501
    """
    advanced: Optional[ConfigAdvanced] = None
    bgp: Optional[ConfigBgp] = None
    cluster: Optional[ConfigCluster] = None
    experiments: Optional[ConfigExperiments] = None
    firewall: Optional[ConfigFirewall] = None
    interfaces: Optional[ConfigInterfaces] = None
    management: Optional[ConfigManagement] = None
    nat: Optional[ConfigNat] = None
    scion: Optional[ConfigSCION] = None
    scion_tunneling: Optional[ConfigScionTunneling] = None
    system: Optional[ConfigSystem] = None
    __properties = ["advanced", "bgp", "cluster", "experiments", "firewall", "interfaces", "management", "nat", "scion", "scion_tunneling", "system"]

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
    def from_json(cls, json_str: str) -> Config:
        """Create an instance of Config from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of advanced
        if self.advanced:
            _dict['advanced'] = self.advanced.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bgp
        if self.bgp:
            _dict['bgp'] = self.bgp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster
        if self.cluster:
            _dict['cluster'] = self.cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of experiments
        if self.experiments:
            _dict['experiments'] = self.experiments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firewall
        if self.firewall:
            _dict['firewall'] = self.firewall.to_dict()
        # override the default output from pydantic by calling `to_dict()` of interfaces
        if self.interfaces:
            _dict['interfaces'] = self.interfaces.to_dict()
        # override the default output from pydantic by calling `to_dict()` of management
        if self.management:
            _dict['management'] = self.management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nat
        if self.nat:
            _dict['nat'] = self.nat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scion
        if self.scion:
            _dict['scion'] = self.scion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scion_tunneling
        if self.scion_tunneling:
            _dict['scion_tunneling'] = self.scion_tunneling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system
        if self.system:
            _dict['system'] = self.system.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Config:
        """Create an instance of Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Config.parse_obj(obj)

        _obj = Config.parse_obj({
            "advanced": ConfigAdvanced.from_dict(obj.get("advanced")) if obj.get("advanced") is not None else None,
            "bgp": ConfigBgp.from_dict(obj.get("bgp")) if obj.get("bgp") is not None else None,
            "cluster": ConfigCluster.from_dict(obj.get("cluster")) if obj.get("cluster") is not None else None,
            "experiments": ConfigExperiments.from_dict(obj.get("experiments")) if obj.get("experiments") is not None else None,
            "firewall": ConfigFirewall.from_dict(obj.get("firewall")) if obj.get("firewall") is not None else None,
            "interfaces": ConfigInterfaces.from_dict(obj.get("interfaces")) if obj.get("interfaces") is not None else None,
            "management": ConfigManagement.from_dict(obj.get("management")) if obj.get("management") is not None else None,
            "nat": ConfigNat.from_dict(obj.get("nat")) if obj.get("nat") is not None else None,
            "scion": ConfigSCION.from_dict(obj.get("scion")) if obj.get("scion") is not None else None,
            "scion_tunneling": ConfigScionTunneling.from_dict(obj.get("scion_tunneling")) if obj.get("scion_tunneling") is not None else None,
            "system": ConfigSystem.from_dict(obj.get("system")) if obj.get("system") is not None else None
        })
        return _obj


