# TRCForLocalISDAvailableInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validity** | [**SchemasValidity**](SchemasValidity.md) |  | 
**grace_period_end** | **datetime** | The time until the previous unexpired version of the TRC should be considered active.  | 
**data_type** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_info import TRCForLocalISDAvailableInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TRCForLocalISDAvailableInfo from a JSON string
trc_for_local_isd_available_info_instance = TRCForLocalISDAvailableInfo.from_json(json)
# print the JSON string representation of the object
print TRCForLocalISDAvailableInfo.to_json()

# convert the object into a dict
trc_for_local_isd_available_info_dict = trc_for_local_isd_available_info_instance.to_dict()
# create an instance of TRCForLocalISDAvailableInfo from a dict
trc_for_local_isd_available_info_form_dict = trc_for_local_isd_available_info.from_dict(trc_for_local_isd_available_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


