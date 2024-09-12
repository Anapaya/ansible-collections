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
from pydantic import StrictStr
from pydantic import Field
from openapi_client.models.certificate_chain_for_as_available import CertificateChainForASAvailable
from openapi_client.models.certificate_chain_for_as_available_data import CertificateChainForASAvailableData
from openapi_client.models.health_component import HealthComponent
from openapi_client.models.health_status import HealthStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CertificateChainForASAvailableWrapped(CertificateChainForASAvailable):
    """
    CertificateChainForASAvailableWrapped
    """ # noqa: E501
    component: HealthComponent
    service_name: StrictStr = Field(description="Name of the service that the health check applies to.")
    __properties: ClassVar[List[str]] = ["check_id", "name", "status", "detail", "data", "component", "service_name"]

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
        """Create an instance of CertificateChainForASAvailableWrapped from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CertificateChainForASAvailableWrapped from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "check_id": obj.get("check_id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "detail": obj.get("detail"),
            "data": CertificateChainForASAvailableData.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "component": obj.get("component"),
            "service_name": obj.get("service_name")
        })
        return _obj


