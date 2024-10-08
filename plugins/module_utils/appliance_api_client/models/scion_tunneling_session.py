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
from ansible.module_utils.appliance_api_client.models.encryption_mode import EncryptionMode
from ansible.module_utils.appliance_api_client.models.scion_tunneling_session_path import ScionTunnelingSessionPath
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScionTunnelingSession(BaseModel):
    """
    ScionTunnelingSession
    """ # noqa: E501
    session_id: StrictStr = Field(description="Unique ID identifying the session.")
    session_id_legacy: StrictInt = Field(description="Unique ID identifying the session.")
    local_isd_as: Annotated[str, Field(strict=True)]
    remote_isd_as: Annotated[str, Field(strict=True)]
    data_addr: Optional[StrictStr] = Field(default=None, description="IP address and port used to send data to the remote end of the tunnel.")
    probe_addr: StrictStr = Field(description="IP address and port used to probe the remote end of the tunnel.")
    pinned: List[StrictInt] = Field(description="A list of remote SCION interfaces that can be used by this session. If empty, any remote SCION interface can be used. ")
    domain: StrictStr = Field(description="The domain this session is used to access.")
    traffic_matcher: StrictStr = Field(description="The class of IP packets this session is used to handle.")
    path_filter: StrictStr = Field(description="The path filter specifies which SCION paths can be used by this session.")
    healthy: StrictBool = Field(description="True if heartbeats are being received from the remote end of the tunnel.")
    encryption: EncryptionMode
    paths: List[ScionTunnelingSessionPath] = Field(description="A list of SCION paths eligible for this session.")
    __properties: ClassVar[List[str]] = ["session_id", "session_id_legacy", "local_isd_as", "remote_isd_as", "data_addr", "probe_addr", "pinned", "domain", "traffic_matcher", "path_filter", "healthy", "encryption", "paths"]

    @field_validator('local_isd_as')
    def local_isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
        return value

    @field_validator('remote_isd_as')
    def remote_isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
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
        """Create an instance of ScionTunnelingSession from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in paths (list)
        _items = []
        if self.paths:
            for _item in self.paths:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paths'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScionTunnelingSession from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "session_id": obj.get("session_id"),
            "session_id_legacy": obj.get("session_id_legacy"),
            "local_isd_as": obj.get("local_isd_as"),
            "remote_isd_as": obj.get("remote_isd_as"),
            "data_addr": obj.get("data_addr"),
            "probe_addr": obj.get("probe_addr"),
            "pinned": obj.get("pinned"),
            "domain": obj.get("domain"),
            "traffic_matcher": obj.get("traffic_matcher"),
            "path_filter": obj.get("path_filter"),
            "healthy": obj.get("healthy"),
            "encryption": obj.get("encryption"),
            "paths": [ScionTunnelingSessionPath.from_dict(_item) for _item in obj.get("paths")] if obj.get("paths") is not None else None
        })
        return _obj


