# TracerouteSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | [**Path**](Path.md) |  | 
**hops** | [**List[TracerouteHopInfo]**](TracerouteHopInfo.md) | Information and statistics for each SCION path hop. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.traceroute_summary import TracerouteSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteSummary from a JSON string
traceroute_summary_instance = TracerouteSummary.from_json(json)
# print the JSON string representation of the object
print TracerouteSummary.to_json()

# convert the object into a dict
traceroute_summary_dict = traceroute_summary_instance.to_dict()
# create an instance of TracerouteSummary from a dict
traceroute_summary_form_dict = traceroute_summary.from_dict(traceroute_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


