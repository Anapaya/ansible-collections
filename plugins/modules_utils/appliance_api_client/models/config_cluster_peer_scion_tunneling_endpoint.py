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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from openapi_client.models.config_cluster_peer_scion_tunneling_endpoint_allowed_interfaces import ConfigClusterPeerScionTunnelingEndpointAllowedInterfaces
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigClusterPeerScionTunnelingEndpoint(BaseModel):
    """
    The SCION tunneling endpoint on the peer appliance.
    """ # noqa: E501
    allowed_interfaces: Optional[List[ConfigClusterPeerScionTunnelingEndpointAllowedInterfaces]] = Field(default=None, description="The SCION interfaces for each SCION AS that is configured on the peer, that are allowed to be used by this IP-in-SCION tunneling endpoint. This can be used to control incoming traffic, e.g., if a tunnel endpoint should only be reachable via SCION interfaces 1 and 2, allowed-interfaces should list them explicitly. Remote tunnel endpoints will then only choose paths entering the respective local AS via SCION interface 1 or 2. If the IP-in-SCION tunneling endpoint on the peer appliance should be reachable via a SCION interface of another appliance, the allowed-interfaces list must be configured with the respective SCION interfaces. By default the list is empty, in this case the appliance will automatically configure the SCION interfaces that are configured on the peer as allowed-interfaces. Automatic configuration can be disabled by setting disable_auto_allowed_interfaces.")
    control_port: Optional[StrictInt] = Field(default=None, description="Port number for control traffic. The control address is constructed from the IP address and this control port. The control address is used to exchange IP routing information as part of SGRP. If not set, or zero, the control port will be dynamically allocated.")
    data_port: Optional[StrictInt] = Field(default=None, description="Port number for data traffic. The data address is constructed from the IP address and this control port. The data address is used for the IP-in-SCION encapsulated traffic stream. If not set, or zero, the data port will be dynamically allocated.")
    disable_auto_allowed_interfaces: Optional[StrictBool] = Field(default=None, description="Whether the automatic configuration of allowed interfaces should be disabled. When disabled, the IP-in-SCION tunneling endpoint of the peer will be reached by remote endpoints on all SCION interfaces of the locally configured AS. When enabled (default), the peer IP-in-SCION tunneling endpoint will only be reached by remote endpoints on the SCION interfaces that are configured on the peer appliance.")
    ip: Optional[StrictStr] = Field(default=None, description="IP address of the peer IP-in-SCION endpoint.")
    probe_port: Optional[StrictInt] = Field(default=None, description="Port number for probing traffic. The probe address is constructed from the IP address and this probe port. The probe address is used by remote tunnel endpoints in their health probing. If not set, or zero, the probe port will be dynamically allocated.")
    __properties: ClassVar[List[str]] = ["allowed_interfaces", "control_port", "data_port", "disable_auto_allowed_interfaces", "ip", "probe_port"]

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
        """Create an instance of ConfigClusterPeerScionTunnelingEndpoint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_interfaces (list)
        _items = []
        if self.allowed_interfaces:
            for _item in self.allowed_interfaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allowed_interfaces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigClusterPeerScionTunnelingEndpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowed_interfaces": [ConfigClusterPeerScionTunnelingEndpointAllowedInterfaces.from_dict(_item) for _item in obj.get("allowed_interfaces")] if obj.get("allowed_interfaces") is not None else None,
            "control_port": obj.get("control_port"),
            "data_port": obj.get("data_port"),
            "disable_auto_allowed_interfaces": obj.get("disable_auto_allowed_interfaces"),
            "ip": obj.get("ip"),
            "probe_port": obj.get("probe_port")
        })
        return _obj


