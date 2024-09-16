# ConfigScionTunnelingStaticAnnouncementNextHopTracking

container for next hop tracking

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether or not this next-hop is tracked. | [optional] 
**target** | **str** | The routes are only distributed if the address responds to pings. This can be used to implement dynamically retractable routes without having to resort to a dynamic routing protocol. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_static_announcement_next_hop_tracking import ConfigScionTunnelingStaticAnnouncementNextHopTracking

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingStaticAnnouncementNextHopTracking from a JSON string
config_scion_tunneling_static_announcement_next_hop_tracking_instance = ConfigScionTunnelingStaticAnnouncementNextHopTracking.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingStaticAnnouncementNextHopTracking.to_json()

# convert the object into a dict
config_scion_tunneling_static_announcement_next_hop_tracking_dict = config_scion_tunneling_static_announcement_next_hop_tracking_instance.to_dict()
# create an instance of ConfigScionTunnelingStaticAnnouncementNextHopTracking from a dict
config_scion_tunneling_static_announcement_next_hop_tracking_form_dict = config_scion_tunneling_static_announcement_next_hop_tracking.from_dict(config_scion_tunneling_static_announcement_next_hop_tracking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


