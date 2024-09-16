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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LanStatsGateway(BaseModel):
    """
    LanStatsGateway
    """ # noqa: E501
    probe_address: StrictStr = Field(description="IP address and port used to send probes to the gateway.")
    local_isd_as: Annotated[str, Field(strict=True)]
    alive: StrictBool = Field(description="True if probes are replied to by the gateway.")
    latency: Union[StrictFloat, StrictInt] = Field(description="The median round-trip latency to the gateway, in milliseconds.")
    jitter: Union[StrictFloat, StrictInt] = Field(description="The jitter of the probes to the gateway, in milliseconds.")
    last_success_time: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["probe_address", "local_isd_as", "alive", "latency", "jitter", "last_success_time"]

    @field_validator('local_isd_as')
    def local_isd_as_validate_regular_expression(cls, value):
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
        """Create an instance of LanStatsGateway from a JSON string"""
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
        """Create an instance of LanStatsGateway from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "probe_address": obj.get("probe_address"),
            "local_isd_as": obj.get("local_isd_as"),
            "alive": obj.get("alive"),
            "latency": obj.get("latency"),
            "jitter": obj.get("jitter"),
            "last_success_time": obj.get("last_success_time")
        })
        return _obj


