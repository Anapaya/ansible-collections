# coding: utf-8

"""
    Appliance Management API

    Management API for the Anapaya EDGE, CORE and GATE appliances

    The version of the OpenAPI document: v0.37.1
    Contact: ops@anapaya.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class LinkState(str, Enum):
    """
    LinkState
    """

    """
    allowed enum values
    """
    UP = 'UP'
    DOWN = 'DOWN'

    @classmethod
    def from_json(cls, json_str: str) -> LinkState:
        """Create an instance of LinkState from a JSON string"""
        return LinkState(json.loads(json_str))


