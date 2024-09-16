# PingUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scion_packet_size** | **int** | Size of the entire SCION packet in bytes. This includes the SCION common header, and the SCION path header. | 
**source_isd_as** | **str** |  | 
**source_host** | **str** | Source host address | 
**scmp_seq** | **int** | SCMP sequence number | 
**round_trip_time** | **str** |  | 
**state** | **str** | Status describing the outcome of a ping response. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.ping_update import PingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PingUpdate from a JSON string
ping_update_instance = PingUpdate.from_json(json)
# print the JSON string representation of the object
print PingUpdate.to_json()

# convert the object into a dict
ping_update_dict = ping_update_instance.to_dict()
# create an instance of PingUpdate from a dict
ping_update_form_dict = ping_update.from_dict(ping_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


