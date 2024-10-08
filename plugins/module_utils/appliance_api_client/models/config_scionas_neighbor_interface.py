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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ansible.module_utils.appliance_api_client.models.config_scionas_neighbor_interface_bfd import ConfigSCIONASNeighborInterfaceBFD
from ansible.module_utils.appliance_api_client.models.config_scionas_neighbor_interface_remote import ConfigSCIONASNeighborInterfaceRemote
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigSCIONASNeighborInterface(BaseModel):
    """
    SCION interface that links to the neighbor AS.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="UDP/IP underlay endpoint of the SCION Interface. The data plane traffic is received on this address. The address must be specified as host:port. Both host and port must be specified.")
    administrative_state: Optional[StrictStr] = Field(default=None, description="Administrative state of the SCION interface.  Experimental: Currently only UP is supported.")
    bfd: Optional[ConfigSCIONASNeighborInterfaceBFD] = None
    description: Optional[StrictStr] = Field(default=None, description="Description, or comment, for the SCION interface.")
    enable_scion_rss: Optional[StrictBool] = Field(default=None, description="Flag to activate SCION RSS for this link. If activated, the router utilizes UDP source port entropy on the underlay such that the remote router can leverage RSS for SCION traffic. This can greatly improve throughput performance. Only enable it if the remote router supports SCION RSS.")
    interface_id: Annotated[int, Field(le=0, strict=True, ge=1)] = Field(description="SCION interface identifier. It must be unique in the SCION AS.")
    remote: Optional[ConfigSCIONASNeighborInterfaceRemote] = None
    scion_mtu: Optional[StrictInt] = Field(default=1472, description="The maximum transmission unit in bytes for SCION packets. This represents the protocol data unit (PDU) of the SCION layer on this interface and is usually calculated as maximum Ethernet payload - IP Header - UDP Header. ")
    __properties: ClassVar[List[str]] = ["address", "administrative_state", "bfd", "description", "enable_scion_rss", "interface_id", "remote", "scion_mtu"]

    @field_validator('administrative_state')
    def administrative_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('UP', 'ADMIN_DOWN', 'DATAPLANE_ONLY'):
            raise ValueError("must be one of enum values ('UP', 'ADMIN_DOWN', 'DATAPLANE_ONLY')")
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
        """Create an instance of ConfigSCIONASNeighborInterface from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bfd
        if self.bfd:
            _dict['bfd'] = self.bfd.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote
        if self.remote:
            _dict['remote'] = self.remote.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigSCIONASNeighborInterface from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "administrative_state": obj.get("administrative_state"),
            "bfd": ConfigSCIONASNeighborInterfaceBFD.from_dict(obj.get("bfd")) if obj.get("bfd") is not None else None,
            "description": obj.get("description"),
            "enable_scion_rss": obj.get("enable_scion_rss"),
            "interface_id": obj.get("interface_id"),
            "remote": ConfigSCIONASNeighborInterfaceRemote.from_dict(obj.get("remote")) if obj.get("remote") is not None else None,
            "scion_mtu": obj.get("scion_mtu") if obj.get("scion_mtu") is not None else 1472
        })
        return _obj


