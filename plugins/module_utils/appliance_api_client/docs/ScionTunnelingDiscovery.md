# ScionTunnelingDiscovery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[ScionTunnelingDiscoverySession]**](ScionTunnelingDiscoverySession.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_discovery import ScionTunnelingDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingDiscovery from a JSON string
scion_tunneling_discovery_instance = ScionTunnelingDiscovery.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingDiscovery.to_json()

# convert the object into a dict
scion_tunneling_discovery_dict = scion_tunneling_discovery_instance.to_dict()
# create an instance of ScionTunnelingDiscovery from a dict
scion_tunneling_discovery_form_dict = scion_tunneling_discovery.from_dict(scion_tunneling_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


