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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigSystemResourcesServiceLimit(BaseModel):
    """
    Per service resource limits.
    """ # noqa: E501
    cpu: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The CPU limit in number of fractional CPU cores that can be used by the service. If not specified, a sensible default is chosen by the system. If set to 0, the service is not limited in terms of CPU usage.")
    memory: Optional[StrictStr] = Field(default=None, description="The memory limit in bytes that can be used by the service. The limit can be specified using a string of the format <decimal><suffix>, where suffix can either be empty or one of 'K', 'k', 'M', 'm', 'G', 'g' or 'T', 't'. Note that the step between the suffixes is 1024. If not specified, a sensible default is chosen by the system. If set to 0, the service is not limited in terms of memory usage. The minimum value is 6M.")
    name: StrictStr = Field(description="Name of the service.")
    __properties: ClassVar[List[str]] = ["cpu", "memory", "name"]

    @field_validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CONTROL', 'ROUTER', 'DISPATCHER', 'DAEMON', 'GATEWAY', 'CA_FRONTEND', 'DATAPLANE_CONTROL', 'MOLE', 'CRON', 'TELEMETRY', 'FRR', 'FRR_EXPORTER', 'NODE_EXPORTER', 'PROMTAIL'):
            raise ValueError("must be one of enum values ('CONTROL', 'ROUTER', 'DISPATCHER', 'DAEMON', 'GATEWAY', 'CA_FRONTEND', 'DATAPLANE_CONTROL', 'MOLE', 'CRON', 'TELEMETRY', 'FRR', 'FRR_EXPORTER', 'NODE_EXPORTER', 'PROMTAIL')")
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
        """Create an instance of ConfigSystemResourcesServiceLimit from a JSON string"""
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
        """Create an instance of ConfigSystemResourcesServiceLimit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpu": obj.get("cpu"),
            "memory": obj.get("memory"),
            "name": obj.get("name")
        })
        return _obj


