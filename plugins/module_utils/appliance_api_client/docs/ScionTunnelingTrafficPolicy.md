# ScionTunnelingTrafficPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_matcher** | **str** | The name of the corresponding traffic matcher. | 
**failover_sequence** | **List[str]** | A failover sequence - the list of path policies. If there are no healthy sessions in the first entry, the second one is used and so on.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_traffic_policy import ScionTunnelingTrafficPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingTrafficPolicy from a JSON string
scion_tunneling_traffic_policy_instance = ScionTunnelingTrafficPolicy.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingTrafficPolicy.to_json()

# convert the object into a dict
scion_tunneling_traffic_policy_dict = scion_tunneling_traffic_policy_instance.to_dict()
# create an instance of ScionTunnelingTrafficPolicy from a dict
scion_tunneling_traffic_policy_form_dict = scion_tunneling_traffic_policy.from_dict(scion_tunneling_traffic_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


