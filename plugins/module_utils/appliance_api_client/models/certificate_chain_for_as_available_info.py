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

from datetime import datetime
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ansible.module_utils.appliance_api_client.models.schemas_validity import SchemasValidity
from ansible.module_utils.appliance_api_client.models.trc_info import TRCInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CertificateChainForASAvailableInfo(BaseModel):
    """
    CertificateChainForASAvailableInfo
    """ # noqa: E501
    isd_as: Annotated[str, Field(strict=True)]
    subject_key_id: StrictStr = Field(description="The subject key identifier of the AS certificate.")
    issuer: Annotated[str, Field(strict=True)]
    valid_until: datetime = Field(description="The time until the certificate is valid for. This is the minimum of the validity.not_before and the trc.validity.not_before time. A certificate chain is only cosidered valid for as long as the TRC that contains the corresponding root certificate is valid. ")
    in_grace_period: StrictBool = Field(description="Indicates if the certificate is only verifiable with a TRC that is currently in grace period. As soon as the grace period expires, the certificate will be considered invalid. ")
    validity: SchemasValidity
    trc: TRCInfo
    data_type: StrictStr
    __properties: ClassVar[List[str]] = ["isd_as", "subject_key_id", "issuer", "valid_until", "in_grace_period", "validity", "trc", "data_type"]

    @field_validator('isd_as')
    def isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
        return value

    @field_validator('issuer')
    def issuer_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
        return value

    @field_validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('available'):
            raise ValueError("must be one of enum values ('available')")
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
        """Create an instance of CertificateChainForASAvailableInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validity
        if self.validity:
            _dict['validity'] = self.validity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trc
        if self.trc:
            _dict['trc'] = self.trc.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CertificateChainForASAvailableInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isd_as": obj.get("isd_as"),
            "subject_key_id": obj.get("subject_key_id"),
            "issuer": obj.get("issuer"),
            "valid_until": obj.get("valid_until"),
            "in_grace_period": obj.get("in_grace_period"),
            "validity": SchemasValidity.from_dict(obj.get("validity")) if obj.get("validity") is not None else None,
            "trc": TRCInfo.from_dict(obj.get("trc")) if obj.get("trc") is not None else None,
            "data_type": obj.get("data_type")
        })
        return _obj


