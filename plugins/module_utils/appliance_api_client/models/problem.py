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
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Problem(BaseModel):
    """
    Problem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default='about:blank', description="A URI reference that uniquely identifies the problem type only in the context of the provided API. Opposed to the specification in RFC-7807, it is neither recommended to be dereferencable and point to a human-readable documentation nor globally unique for the problem type.")
    title: StrictStr = Field(description="A short summary of the problem type. Written in English and readable for engineers, usually not suited for non technical stakeholders and not localized.")
    status: Annotated[int, Field(le=599, strict=True, ge=100)] = Field(description="The HTTP status code generated by the origin server for this occurrence of the problem.")
    detail: Optional[StrictStr] = Field(default=None, description="A human readable explanation specific to this occurrence of the problem that is helpful to locate the problem and give advice on how to proceed. Written in English and readable for engineers, usually not suited for non technical stakeholders and not localized.")
    instance: Optional[StrictStr] = Field(default=None, description="A URI reference that identifies the specific occurrence of the problem, e.g. by adding a fragment identifier or sub-path to the problem type. May be used to locate the root of this problem in the source code.")
    __properties: ClassVar[List[str]] = ["type", "title", "status", "detail", "instance"]

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
        """Create an instance of Problem from a JSON string"""
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
        """Create an instance of Problem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'about:blank',
            "title": obj.get("title"),
            "status": obj.get("status"),
            "detail": obj.get("detail"),
            "instance": obj.get("instance")
        })
        return _obj


