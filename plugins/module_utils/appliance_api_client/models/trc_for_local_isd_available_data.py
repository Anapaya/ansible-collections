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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_info import TRCForLocalISDAvailableInfo
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_not_found import TRCForLocalISDAvailableNotFound
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

TRCFORLOCALISDAVAILABLEDATA_ONE_OF_SCHEMAS = ["TRCForLocalISDAvailableInfo", "TRCForLocalISDAvailableNotFound"]

class TRCForLocalISDAvailableData(BaseModel):
    """
    The TRC for the local ISD is available in the SCION control service. A TRC is required to establish trust in the SCION network. The TRC is used to verify the CPPKI certificates which are used to sign the SCION control plane messages. If the TRC is not present, the local AS will not be able to connect to the SCION network. 
    """
    # data type: TRCForLocalISDAvailableInfo
    oneof_schema_1_validator: Optional[TRCForLocalISDAvailableInfo] = None
    # data type: TRCForLocalISDAvailableNotFound
    oneof_schema_2_validator: Optional[TRCForLocalISDAvailableNotFound] = None
    actual_instance: Optional[Union[TRCForLocalISDAvailableInfo, TRCForLocalISDAvailableNotFound]] = None
    one_of_schemas: List[str] = Literal["TRCForLocalISDAvailableInfo", "TRCForLocalISDAvailableNotFound"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TRCForLocalISDAvailableData.model_construct()
        error_messages = []
        match = 0
        # validate data type: TRCForLocalISDAvailableInfo
        if not isinstance(v, TRCForLocalISDAvailableInfo):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TRCForLocalISDAvailableInfo`")
        else:
            match += 1
        # validate data type: TRCForLocalISDAvailableNotFound
        if not isinstance(v, TRCForLocalISDAvailableNotFound):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TRCForLocalISDAvailableNotFound`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TRCForLocalISDAvailableData with oneOf schemas: TRCForLocalISDAvailableInfo, TRCForLocalISDAvailableNotFound. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TRCForLocalISDAvailableData with oneOf schemas: TRCForLocalISDAvailableInfo, TRCForLocalISDAvailableNotFound. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into TRCForLocalISDAvailableInfo
        try:
            instance.actual_instance = TRCForLocalISDAvailableInfo.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TRCForLocalISDAvailableNotFound
        try:
            instance.actual_instance = TRCForLocalISDAvailableNotFound.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TRCForLocalISDAvailableData with oneOf schemas: TRCForLocalISDAvailableInfo, TRCForLocalISDAvailableNotFound. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TRCForLocalISDAvailableData with oneOf schemas: TRCForLocalISDAvailableInfo, TRCForLocalISDAvailableNotFound. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


