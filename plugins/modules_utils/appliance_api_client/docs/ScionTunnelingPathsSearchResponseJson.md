# ScionTunnelingPathsSearchResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | [**List[ScionTunnelingPathDataJson]**](ScionTunnelingPathDataJson.md) | List of paths and their data. | 

## Example

```python
from openapi_client.models.scion_tunneling_paths_search_response_json import ScionTunnelingPathsSearchResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingPathsSearchResponseJson from a JSON string
scion_tunneling_paths_search_response_json_instance = ScionTunnelingPathsSearchResponseJson.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingPathsSearchResponseJson.to_json()

# convert the object into a dict
scion_tunneling_paths_search_response_json_dict = scion_tunneling_paths_search_response_json_instance.to_dict()
# create an instance of ScionTunnelingPathsSearchResponseJson from a dict
scion_tunneling_paths_search_response_json_form_dict = scion_tunneling_paths_search_response_json.from_dict(scion_tunneling_paths_search_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


