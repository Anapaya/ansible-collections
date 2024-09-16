# ConfigScionTunnelingStaticAnnouncement

List of static announcements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description, or comment, for the target. | [optional] 
**next_hop_tracking** | [**ConfigScionTunnelingStaticAnnouncementNextHopTracking**](ConfigScionTunnelingStaticAnnouncementNextHopTracking.md) |  | [optional] 
**prefixes** | **List[str]** | The IP prefixes that are statically configured and advertised via SGRP | 
**sequence_id** | **int** | The sequence ID defines the order of the static route entries. The sequence ID must be unique for each entry. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_static_announcement import ConfigScionTunnelingStaticAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingStaticAnnouncement from a JSON string
config_scion_tunneling_static_announcement_instance = ConfigScionTunnelingStaticAnnouncement.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingStaticAnnouncement.to_json()

# convert the object into a dict
config_scion_tunneling_static_announcement_dict = config_scion_tunneling_static_announcement_instance.to_dict()
# create an instance of ConfigScionTunnelingStaticAnnouncement from a dict
config_scion_tunneling_static_announcement_form_dict = config_scion_tunneling_static_announcement.from_dict(config_scion_tunneling_static_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


