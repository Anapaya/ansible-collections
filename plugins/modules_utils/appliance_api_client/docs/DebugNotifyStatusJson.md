# DebugNotifyStatusJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Whether the appliance-controller notifications are disabled. | 
**indefinite** | **bool** | Whether the appliance-controller notifications are disabled indefinitely. Only one of indefinite, deadline and timeout must be set.  | [optional] [default to False]
**deadline** | **datetime** | Until when appliance-controller notifications are disabled specified as a RFC3339 formatted date-time string. Only one of indefinite, deadline and timeout must be set.  | [optional] 
**timeout** | **str** | Duration during which the appliance-controller notifications are disabled specified as a duration string. A duration string is a possibly signed sequence of decimal numbers, each with optional fraction and a unit suffix, such as \&quot;300ms\&quot;, \&quot;-1.5h\&quot; or \&quot;2h45m\&quot;. Valid time units are \&quot;ns\&quot;, \&quot;us\&quot; (or \&quot;µs\&quot;), \&quot;ms\&quot;, \&quot;s\&quot;, \&quot;m\&quot;, \&quot;h\&quot;. Only one of indefinite, deadline and timeout must be set.  | [optional] 

## Example

```python
from openapi_client.models.debug_notify_status_json import DebugNotifyStatusJson

# TODO update the JSON string below
json = "{}"
# create an instance of DebugNotifyStatusJson from a JSON string
debug_notify_status_json_instance = DebugNotifyStatusJson.from_json(json)
# print the JSON string representation of the object
print DebugNotifyStatusJson.to_json()

# convert the object into a dict
debug_notify_status_json_dict = debug_notify_status_json_instance.to_dict()
# create an instance of DebugNotifyStatusJson from a dict
debug_notify_status_json_form_dict = debug_notify_status_json.from_dict(debug_notify_status_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


