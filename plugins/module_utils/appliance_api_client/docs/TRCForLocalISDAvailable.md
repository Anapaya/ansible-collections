# TRCForLocalISDAvailable

Check data for an explanation of this health check. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TRCForLocalISDAvailableData**](TRCForLocalISDAvailableData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available import TRCForLocalISDAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of TRCForLocalISDAvailable from a JSON string
trc_for_local_isd_available_instance = TRCForLocalISDAvailable.from_json(json)
# print the JSON string representation of the object
print TRCForLocalISDAvailable.to_json()

# convert the object into a dict
trc_for_local_isd_available_dict = trc_for_local_isd_available_instance.to_dict()
# create an instance of TRCForLocalISDAvailable from a dict
trc_for_local_isd_available_form_dict = trc_for_local_isd_available.from_dict(trc_for_local_isd_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


