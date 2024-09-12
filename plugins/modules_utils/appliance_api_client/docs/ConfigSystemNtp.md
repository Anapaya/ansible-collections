# ConfigSystemNtp

Anapaya appliance NTP configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_distance_max** | **str** | Maximum acceptable root distance, i.e. the maximum estimated time required for a packet to travel to the server we are connected to from the server with the reference clock. If the current server does not satisfy this limit, the appliance will switch to a different server. | [optional] [default to '5s']
**servers** | [**List[ConfigSystemNtpServers]**](ConfigSystemNtpServers.md) | List of NTP servers. | [optional] 

## Example

```python
from openapi_client.models.config_system_ntp import ConfigSystemNtp

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemNtp from a JSON string
config_system_ntp_instance = ConfigSystemNtp.from_json(json)
# print the JSON string representation of the object
print ConfigSystemNtp.to_json()

# convert the object into a dict
config_system_ntp_dict = config_system_ntp_instance.to_dict()
# create an instance of ConfigSystemNtp from a dict
config_system_ntp_form_dict = config_system_ntp.from_dict(config_system_ntp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


