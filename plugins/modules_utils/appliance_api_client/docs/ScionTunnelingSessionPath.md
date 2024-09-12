# ScionTunnelingSessionPath

SCION path state specific to a tunneling session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | Fingerprint on the SCION path. | 
**current** | **bool** | Whether the path is currently actively used. | 
**rejected** | **bool** | Whether the path has been rejected by the path filter. | 

## Example

```python
from openapi_client.models.scion_tunneling_session_path import ScionTunnelingSessionPath

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingSessionPath from a JSON string
scion_tunneling_session_path_instance = ScionTunnelingSessionPath.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingSessionPath.to_json()

# convert the object into a dict
scion_tunneling_session_path_dict = scion_tunneling_session_path_instance.to_dict()
# create an instance of ScionTunnelingSessionPath from a dict
scion_tunneling_session_path_form_dict = scion_tunneling_session_path.from_dict(scion_tunneling_session_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


