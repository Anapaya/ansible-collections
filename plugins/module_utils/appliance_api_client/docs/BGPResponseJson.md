# BGPResponseJson


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**BGPConfig**](BGPConfig.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.bgp_response_json import BGPResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of BGPResponseJson from a JSON string
bgp_response_json_instance = BGPResponseJson.from_json(json)
# print the JSON string representation of the object
print BGPResponseJson.to_json()

# convert the object into a dict
bgp_response_json_dict = bgp_response_json_instance.to_dict()
# create an instance of BGPResponseJson from a dict
bgp_response_json_form_dict = bgp_response_json.from_dict(bgp_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


