# ConfigScionTunnelingTrafficMatcher

List of traffic matchers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | The condition for traffic to match this traffic matcher. | 
**description** | **str** | Description, or comment, for the traffic matcher | [optional] 
**name** | **str** | Name that identifies the traffic matcher. This is value is used by the traffic policy to reference the traffic matcher. | 

## Example

```python
from openapi_client.models.config_scion_tunneling_traffic_matcher import ConfigScionTunnelingTrafficMatcher

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingTrafficMatcher from a JSON string
config_scion_tunneling_traffic_matcher_instance = ConfigScionTunnelingTrafficMatcher.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingTrafficMatcher.to_json()

# convert the object into a dict
config_scion_tunneling_traffic_matcher_dict = config_scion_tunneling_traffic_matcher_instance.to_dict()
# create an instance of ConfigScionTunnelingTrafficMatcher from a dict
config_scion_tunneling_traffic_matcher_form_dict = config_scion_tunneling_traffic_matcher.from_dict(config_scion_tunneling_traffic_matcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


