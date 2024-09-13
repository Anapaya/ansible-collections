# TRCForLocalISDAvailableData

The TRC for the local ISD is available in the SCION control service. A TRC is required to establish trust in the SCION network. The TRC is used to verify the CPPKI certificates which are used to sign the SCION control plane messages. If the TRC is not present, the local AS will not be able to connect to the SCION network. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd** | **int** | The ISD of the TRC. | 
**data_type** | **str** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_data import TRCForLocalISDAvailableData

# TODO update the JSON string below
json = "{}"
# create an instance of TRCForLocalISDAvailableData from a JSON string
trc_for_local_isd_available_data_instance = TRCForLocalISDAvailableData.from_json(json)
# print the JSON string representation of the object
print TRCForLocalISDAvailableData.to_json()

# convert the object into a dict
trc_for_local_isd_available_data_dict = trc_for_local_isd_available_data_instance.to_dict()
# create an instance of TRCForLocalISDAvailableData from a dict
trc_for_local_isd_available_data_form_dict = trc_for_local_isd_available_data.from_dict(trc_for_local_isd_available_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


