# BGPNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_asn** | **int** | The AS number of the neighbor in the BGP session. | 
**remote_address** | **str** | The IP address of the neighbor in the BGP session. | 
**timers** | [**BGPTimers**](BGPTimers.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.bgp_neighbor import BGPNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of BGPNeighbor from a JSON string
bgp_neighbor_instance = BGPNeighbor.from_json(json)
# print the JSON string representation of the object
print BGPNeighbor.to_json()

# convert the object into a dict
bgp_neighbor_dict = bgp_neighbor_instance.to_dict()
# create an instance of BGPNeighbor from a dict
bgp_neighbor_form_dict = bgp_neighbor.from_dict(bgp_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


