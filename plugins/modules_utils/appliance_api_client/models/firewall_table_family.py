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
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class FirewallTableFamily(str, Enum):
    """
    The table family of the nftables table.
    """

    """
    allowed enum values
    """
    IP = 'ip'
    IP6 = 'ip6'
    INET = 'inet'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FirewallTableFamily from a JSON string"""
        return cls(json.loads(json_str))


