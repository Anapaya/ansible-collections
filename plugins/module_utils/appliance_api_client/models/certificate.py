# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: v0.37.1
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, constr, validator
from ansible.module_utils.appliance_api_client.models.validity import Validity

class Certificate(BaseModel):
    """
    Certificate
    """
    distinguished_name: StrictStr = Field(...)
    isd_as: constr(strict=True) = Field(...)
    validity: Validity = Field(...)
    subject_key_algo: StrictStr = Field(...)
    subject_key_id: StrictStr = Field(...)
    __properties = ["distinguished_name", "isd_as", "validity", "subject_key_algo", "subject_key_id"]

    @validator('isd_as')
    def isd_as_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+-([a-f0-9]{1,4}:){2}([a-f0-9]{1,4})|\d+$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Certificate:
        """Create an instance of Certificate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of validity
        if self.validity:
            _dict['validity'] = self.validity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Certificate:
        """Create an instance of Certificate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Certificate.parse_obj(obj)

        _obj = Certificate.parse_obj({
            "distinguished_name": obj.get("distinguished_name"),
            "isd_as": obj.get("isd_as"),
            "validity": Validity.from_dict(obj.get("validity")) if obj.get("validity") is not None else None,
            "subject_key_algo": obj.get("subject_key_algo"),
            "subject_key_id": obj.get("subject_key_id")
        })
        return _obj


