# BGPNeighborStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neighbor** | **str** | ID of the neighbor. | 
**remote_as** | **int** | Remote BGP AS number. | 
**family** | **str** | Protocol family. | 
**state** | **str** | State of the session to the neighbor. | 
**uptime** | **int** | Uptime of the session to the neighbor in milliseconds. | 
**number_of_sent_prefixes** | **int** | Number of prefixes sent to the neighbor. | 
**number_of_received_prefixes** | **int** | Number of prefixes received from the neighbor. | 

## Example

```python
from openapi_client.models.bgp_neighbor_status import BGPNeighborStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BGPNeighborStatus from a JSON string
bgp_neighbor_status_instance = BGPNeighborStatus.from_json(json)
# print the JSON string representation of the object
print BGPNeighborStatus.to_json()

# convert the object into a dict
bgp_neighbor_status_dict = bgp_neighbor_status_instance.to_dict()
# create an instance of BGPNeighborStatus from a dict
bgp_neighbor_status_form_dict = bgp_neighbor_status.from_dict(bgp_neighbor_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


