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


from typing import Any, ClassVar, Dict, List, Union
from pydantic import StrictFloat, StrictInt
from pydantic import Field
from ansible.module_utils.appliance_api_client.models.scion_path import ScionPath
from ansible.module_utils.appliance_api_client.models.scion_path_hop import ScionPathHop
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScionPathWithMetrics(ScionPath):
    """
    ScionPathWithMetrics
    """ # noqa: E501
    latency: Union[StrictFloat, StrictInt] = Field(description="The latency of the path, in milliseconds.")
    jitter: Union[StrictFloat, StrictInt] = Field(description="The jitter of the path, in milliseconds.")
    droprate: Union[StrictFloat, StrictInt] = Field(description="The drop rate of the path, percent.")
    throughput_pkts: Union[StrictFloat, StrictInt] = Field(description="The outgoing throughput of the path in packets per second.")
    throughput_bytes: Union[StrictFloat, StrictInt] = Field(description="The outgoing throughput of the path in bytes per second.")
    __properties: ClassVar[List[str]] = ["fingerprint", "human", "hops", "status", "next_hop", "expiration", "mtu", "latency", "jitter", "droprate", "throughput_pkts", "throughput_bytes"]

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
        """Create an instance of ScionPathWithMetrics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in hops (list)
        _items = []
        if self.hops:
            for _item in self.hops:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hops'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScionPathWithMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fingerprint": obj.get("fingerprint"),
            "human": obj.get("human"),
            "hops": [ScionPathHop.from_dict(_item) for _item in obj.get("hops")] if obj.get("hops") is not None else None,
            "status": obj.get("status"),
            "next_hop": obj.get("next_hop"),
            "expiration": obj.get("expiration"),
            "mtu": obj.get("mtu"),
            "latency": obj.get("latency"),
            "jitter": obj.get("jitter"),
            "droprate": obj.get("droprate"),
            "throughput_pkts": obj.get("throughput_pkts"),
            "throughput_bytes": obj.get("throughput_bytes")
        })
        return _obj


