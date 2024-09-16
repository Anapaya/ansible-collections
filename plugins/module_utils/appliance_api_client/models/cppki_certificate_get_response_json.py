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



from pydantic import BaseModel, Field
from ansible.module_utils.appliance_api_client.models.chain import Chain

class CppkiCertificateGetResponseJson(BaseModel):
    """
    CppkiCertificateGetResponseJson
    """
    certificate_chain: Chain = Field(...)
    __properties = ["certificate_chain"]

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
    def from_json(cls, json_str: str) -> CppkiCertificateGetResponseJson:
        """Create an instance of CppkiCertificateGetResponseJson from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of certificate_chain
        if self.certificate_chain:
            _dict['certificate_chain'] = self.certificate_chain.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CppkiCertificateGetResponseJson:
        """Create an instance of CppkiCertificateGetResponseJson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CppkiCertificateGetResponseJson.parse_obj(obj)

        _obj = CppkiCertificateGetResponseJson.parse_obj({
            "certificate_chain": Chain.from_dict(obj.get("certificate_chain")) if obj.get("certificate_chain") is not None else None
        })
        return _obj


