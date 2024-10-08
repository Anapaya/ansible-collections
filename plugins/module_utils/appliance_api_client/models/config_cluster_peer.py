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
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_features import ConfigClusterPeerFeatures
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion import ConfigClusterPeerScion
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_scion_tunneling import ConfigClusterPeerScionTunneling
from ansible.module_utils.appliance_api_client.models.config_cluster_peer_synchronization import ConfigClusterPeerSynchronization
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigClusterPeer(BaseModel):
    """
    The peer of this appliance.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Textual description for this peer.")
    features: Optional[ConfigClusterPeerFeatures] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of this peer used to identify the peer. This can be any string but must be unique among all peers.")
    scion: Optional[ConfigClusterPeerScion] = None
    scion_tunneling: Optional[ConfigClusterPeerScionTunneling] = None
    synchronization: Optional[ConfigClusterPeerSynchronization] = None
    __properties: ClassVar[List[str]] = ["description", "features", "name", "scion", "scion_tunneling", "synchronization"]

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
        """Create an instance of ConfigClusterPeer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scion
        if self.scion:
            _dict['scion'] = self.scion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scion_tunneling
        if self.scion_tunneling:
            _dict['scion_tunneling'] = self.scion_tunneling.to_dict()
        # override the default output from pydantic by calling `to_dict()` of synchronization
        if self.synchronization:
            _dict['synchronization'] = self.synchronization.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigClusterPeer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "features": ConfigClusterPeerFeatures.from_dict(obj.get("features")) if obj.get("features") is not None else None,
            "name": obj.get("name"),
            "scion": ConfigClusterPeerScion.from_dict(obj.get("scion")) if obj.get("scion") is not None else None,
            "scion_tunneling": ConfigClusterPeerScionTunneling.from_dict(obj.get("scion_tunneling")) if obj.get("scion_tunneling") is not None else None,
            "synchronization": ConfigClusterPeerSynchronization.from_dict(obj.get("synchronization")) if obj.get("synchronization") is not None else None
        })
        return _obj


