# TRCForLocalISDAvailableInDaemonData

The TRC for the local ISD is available on the SCION Daemon. A TRC is required to establish trust in the SCION network. The TRC is used to verify the CPPKI certificates which are used to sign the SCION control plane messages. If the TRC is not present, applications on this appliance will not be able to connect to the SCION network. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The TRC identifier composed of the ISD identfier, base and serial number. | [optional] 
**isd** | **int** | The ISD of the TRC. | 
**base** | **int** | The base number of the TRC. Usually 1, unless a trust reset has been performed. | [optional] 
**serial** | **int** | The serial number of the TRC. Incremented with each new TRC. | [optional] 
**not_before** | **datetime** | The time at which the validity period starts. | [optional] 
**not_after** | **datetime** | The time at which the validity period stops. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_in_daemon_data import TRCForLocalISDAvailableInDaemonData

# TODO update the JSON string below
json = "{}"
# create an instance of TRCForLocalISDAvailableInDaemonData from a JSON string
trc_for_local_isd_available_in_daemon_data_instance = TRCForLocalISDAvailableInDaemonData.from_json(json)
# print the JSON string representation of the object
print TRCForLocalISDAvailableInDaemonData.to_json()

# convert the object into a dict
trc_for_local_isd_available_in_daemon_data_dict = trc_for_local_isd_available_in_daemon_data_instance.to_dict()
# create an instance of TRCForLocalISDAvailableInDaemonData from a dict
trc_for_local_isd_available_in_daemon_data_form_dict = trc_for_local_isd_available_in_daemon_data.from_dict(trc_for_local_isd_available_in_daemon_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


