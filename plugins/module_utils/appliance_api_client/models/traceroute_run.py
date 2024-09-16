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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TracerouteRun(BaseModel):
    """
    TracerouteRun
    """ # noqa: E501
    destination_host: StrictStr = Field(description="IPv4 or IPv6 address")
    destination_isd_as: Annotated[str, Field(strict=True)]
    source_isd_as: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="If source_isd_as is unset, then the default ISD-AS from the configuration is used.")
    sequence: Optional[StrictStr] = Field(default=None, description="SCION paths can be filtered according to a sequence. A sequence is a string of space separated HopPredicates. A Hop Predicate (HP) is of the form 'ISD-AS#IF,IF'. The first IF means the inbound interface (the interface where packet enters the AS) and the second IF means the outbound interface (the interface where packet leaves the AS). 0 can be used as a wildcard for ISD, AS and both IF elements independently.  HopPredicate Examples:    - Match any:                               0   - Match ISD 1:                             1   - Match AS 1-ff00:0:133:                   1-ff00:0:133   - Match IF 2 of AS 1-ff00:0:133:           1-ff00:0:133#2   - Match inbound IF 2 of AS 1-ff00:0:133:   1-ff00:0:133#2,0   - Match outbound IF 2 of AS 1-ff00:0:133:  1-ff00:0:133#0,2  Sequence Examples:  ``` sequence: \"1-ff00:0:133#0 1-ff00:0:120#2,1 0 0 1-ff00:0:110#0\" ```  The above example specifies a path from any interface in AS 1-ff00:0:133 to two subsequent interfaces in AS 1-ff00:0:120 (entering on interface 2 and exiting on interface 1), then there are two wildcards that each match any AS. The path must end with any interface in AS 1-ff00:0:110. ```   sequence: \"1-ff00:0:133#1 1+ 2-ff00:0:1? 2-ff00:0:233#1\" ``` The above example includes operators and specifies a path from interface 1-ff00:0:133#1 through multiple ASes in ISD 1, that may (but does not need to) traverse AS 2-ff00:0:1 and then reaches its destination on 2-ff00:0:233#1. Available operators:    - ? (the preceding HopPredicate may appear at most once)   - \\+ (the preceding ISD-level HopPredicate must appear at least once)   - \\* (the preceding ISD-level HopPredicate may appear zero or more times)   - | (logical OR) ")
    timeout: Optional[StrictStr] = Field(default='1s', description="Timeout per packet. Valid time units are \"ms\", \"s\".")
    probes_per_hop: Optional[StrictInt] = Field(default=3, description="Number of probes per hop")
    __properties: ClassVar[List[str]] = ["destination_host", "destination_isd_as", "source_isd_as", "sequence", "timeout", "probes_per_hop"]

    @field_validator('destination_isd_as')
    def destination_isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
        return value

    @field_validator('source_isd_as')
    def source_isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of TracerouteRun from a JSON string"""
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
        """Create an instance of TracerouteRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "destination_host": obj.get("destination_host"),
            "destination_isd_as": obj.get("destination_isd_as"),
            "source_isd_as": obj.get("source_isd_as"),
            "sequence": obj.get("sequence"),
            "timeout": obj.get("timeout") if obj.get("timeout") is not None else '1s',
            "probes_per_hop": obj.get("probes_per_hop") if obj.get("probes_per_hop") is not None else 3
        })
        return _obj


