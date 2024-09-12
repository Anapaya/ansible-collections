# TracerouteHopInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd_as** | **str** |  | 
**ip** | **str** | IP address of the router responding to the traceroute request. | 
**interface_id** | **int** | SCION interface identifier. | 
**round_trip_times** | **List[str]** |  | 

## Example

```python
from openapi_client.models.traceroute_hop_info import TracerouteHopInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteHopInfo from a JSON string
traceroute_hop_info_instance = TracerouteHopInfo.from_json(json)
# print the JSON string representation of the object
print TracerouteHopInfo.to_json()

# convert the object into a dict
traceroute_hop_info_dict = traceroute_hop_info_instance.to_dict()
# create an instance of TracerouteHopInfo from a dict
traceroute_hop_info_form_dict = traceroute_hop_info.from_dict(traceroute_hop_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


