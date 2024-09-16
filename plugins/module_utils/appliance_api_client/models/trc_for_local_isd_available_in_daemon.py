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



from pydantic import Field
from ansible.module_utils.appliance_api_client.models.base_health_check import BaseHealthCheck
from ansible.module_utils.appliance_api_client.models.health_status import HealthStatus
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_in_daemon_data import TRCForLocalISDAvailableInDaemonData

class TRCForLocalISDAvailableInDaemon(BaseHealthCheck):
    """
    Check data for an explanation of this health check.   # noqa: E501
    """
    data: TRCForLocalISDAvailableInDaemonData = Field(...)
    __properties = ["check_id", "name", "status", "detail", "data"]

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
    def from_json(cls, json_str: str) -> TRCForLocalISDAvailableInDaemon:
        """Create an instance of TRCForLocalISDAvailableInDaemon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TRCForLocalISDAvailableInDaemon:
        """Create an instance of TRCForLocalISDAvailableInDaemon from a dict"""


