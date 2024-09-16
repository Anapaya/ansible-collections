# ScionTunnelingFailoverSequenceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path_filter_name** | **str** | Name of the path filter used for this failover entry. | 
**sessions** | **List[str]** | A list of session IDs used by this failover entry. | 
**sessions_legacy** | **List[int]** | A list of session IDs used by this failover entry. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_failover_sequence_entry import ScionTunnelingFailoverSequenceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingFailoverSequenceEntry from a JSON string
scion_tunneling_failover_sequence_entry_instance = ScionTunnelingFailoverSequenceEntry.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingFailoverSequenceEntry.to_json()

# convert the object into a dict
scion_tunneling_failover_sequence_entry_dict = scion_tunneling_failover_sequence_entry_instance.to_dict()
# create an instance of ScionTunnelingFailoverSequenceEntry from a dict
scion_tunneling_failover_sequence_entry_form_dict = scion_tunneling_failover_sequence_entry.from_dict(scion_tunneling_failover_sequence_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


