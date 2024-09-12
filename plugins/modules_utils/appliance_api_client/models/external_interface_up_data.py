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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from openapi_client.models.link_relationship import LinkRelationship
from openapi_client.models.link_state import LinkState
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExternalInterfaceUpData(BaseModel):
    """
    The external interface to a neighboring SCION AS is up.  If the interface is configured with BFD enabled, the health check reports up if the BFD session is up. If BFD is not enabled, the health check always reports up. 
    """ # noqa: E501
    local_isd_as: Annotated[str, Field(strict=True)]
    local_address: StrictStr = Field(description="The local underaly UDP address.")
    local_interface: StrictInt = Field(description="The local interface identifier.")
    remote_isd_as: Annotated[str, Field(strict=True)]
    remote_address: StrictStr = Field(description="The remote underaly UDP address.")
    remote_interface: StrictInt = Field(description="The remote interface identifier.")
    relationship: LinkRelationship
    state: LinkState
    bfd_enabled: StrictBool = Field(description="Whether BFD is enabled on the interface.")
    __properties: ClassVar[List[str]] = ["local_isd_as", "local_address", "local_interface", "remote_isd_as", "remote_address", "remote_interface", "relationship", "state", "bfd_enabled"]

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
        """Create an instance of ExternalInterfaceUpData from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExternalInterfaceUpData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "local_isd_as": obj.get("local_isd_as"),
            "local_address": obj.get("local_address"),
            "local_interface": obj.get("local_interface"),
            "remote_isd_as": obj.get("remote_isd_as"),
            "remote_address": obj.get("remote_address"),
            "remote_interface": obj.get("remote_interface"),
            "relationship": obj.get("relationship"),
            "state": obj.get("state"),
            "bfd_enabled": obj.get("bfd_enabled")
        })
        return _obj


