# ScionTunnelingTrafficMatcher


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_policy_id** | **int** | Unique ID of this traffic class. | 
**traffic_matcher** | **str** | Name of the corresponding traffic matcher. | 
**failover_sequence** | [**List[ScionTunnelingFailoverSequenceEntry]**](ScionTunnelingFailoverSequenceEntry.md) | A failover sequence. If there are no healthy sessions in the first entry, the second one is used and so on.  | 
**selected_session** | **str** | The ID of the session currently used to handle this traffic class. | 
**selected_session_legacy** | **int** | The ID of the session currently used to handle this traffic class. | 
**selected_path** | **str** | The SCION path currently used to handle this traffic class. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_traffic_matcher import ScionTunnelingTrafficMatcher

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingTrafficMatcher from a JSON string
scion_tunneling_traffic_matcher_instance = ScionTunnelingTrafficMatcher.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingTrafficMatcher.to_json()

# convert the object into a dict
scion_tunneling_traffic_matcher_dict = scion_tunneling_traffic_matcher_instance.to_dict()
# create an instance of ScionTunnelingTrafficMatcher from a dict
scion_tunneling_traffic_matcher_form_dict = scion_tunneling_traffic_matcher.from_dict(scion_tunneling_traffic_matcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


