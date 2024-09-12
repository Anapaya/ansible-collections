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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigSCIONASCAServiceExternal(BaseModel):
    """
    The configuration data for the External SCION CPPKI CA service. This section is provided only when the CA service is of type External, i.e., is not operated by Anapaya.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="The address where the external SCION CPPKI CA service can be reached.")
    client_id: Optional[StrictStr] = Field(default=None, description="The client ID that is used to authenticate with the CA service. The client ID is set in the 'sub' and 'iss' claim of the generated JWT. If unset, a generic client ID based on the ISD-AS is used.")
    shared_secret: Optional[StrictStr] = Field(default=None, description="The shared secrets between the appliance and the CA service (used to generate JWTs for authentication).")
    __properties: ClassVar[List[str]] = ["address", "client_id", "shared_secret"]

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
        """Create an instance of ConfigSCIONASCAServiceExternal from a JSON string"""
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
        """Create an instance of ConfigSCIONASCAServiceExternal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "client_id": obj.get("client_id"),
            "shared_secret": obj.get("shared_secret")
        })
        return _obj


