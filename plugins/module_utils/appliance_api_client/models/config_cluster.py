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
from ansible.module_utils.appliance_api_client.models.config_cluster_features import ConfigClusterFeatures
from ansible.module_utils.appliance_api_client.models.config_cluster_peer import ConfigClusterPeer
from ansible.module_utils.appliance_api_client.models.config_cluster_synchronization import ConfigClusterSynchronization

class ConfigCluster(BaseModel):
    """
    The configuration for the appliance cluster.  # noqa: E501
    """
    features: Optional[ConfigClusterFeatures] = None
    peers: Optional[conlist(ConfigClusterPeer)] = Field(None, description="The list of peers in this cluster. This is used to configure the topology or the discovery of the topology of peer appliances in an organization.")
    synchronization: Optional[ConfigClusterSynchronization] = None
    __properties = ["features", "peers", "synchronization"]

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
    def from_json(cls, json_str: str) -> ConfigCluster:
        """Create an instance of ConfigCluster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in peers (list)
        _items = []
        if self.peers:
            for _item in self.peers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['peers'] = _items
        # override the default output from pydantic by calling `to_dict()` of synchronization
        if self.synchronization:
            _dict['synchronization'] = self.synchronization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigCluster:
        """Create an instance of ConfigCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigCluster.parse_obj(obj)

        _obj = ConfigCluster.parse_obj({
            "features": ConfigClusterFeatures.from_dict(obj.get("features")) if obj.get("features") is not None else None,
            "peers": [ConfigClusterPeer.from_dict(_item) for _item in obj.get("peers")] if obj.get("peers") is not None else None,
            "synchronization": ConfigClusterSynchronization.from_dict(obj.get("synchronization")) if obj.get("synchronization") is not None else None
        })
        return _obj


