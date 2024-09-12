# BGPNeighborsResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neighbors** | [**List[BGPNeighborStatus]**](BGPNeighborStatus.md) |  | 

## Example

```python
from openapi_client.models.bgp_neighbors_response_json import BGPNeighborsResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of BGPNeighborsResponseJson from a JSON string
bgp_neighbors_response_json_instance = BGPNeighborsResponseJson.from_json(json)
# print the JSON string representation of the object
print BGPNeighborsResponseJson.to_json()

# convert the object into a dict
bgp_neighbors_response_json_dict = bgp_neighbors_response_json_instance.to_dict()
# create an instance of BGPNeighborsResponseJson from a dict
bgp_neighbors_response_json_form_dict = bgp_neighbors_response_json.from_dict(bgp_neighbors_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


