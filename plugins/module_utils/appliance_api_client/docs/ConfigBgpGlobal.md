# ConfigBgpGlobal

Global configuration for the BGP router

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_as** | **int** | Local BGP autonomous system number of the router. Uses the 32-bit as-number type from the model in RFC 6991. | [optional] 
**networks** | **List[str]** | The list of network prefixes this BGP instance advertises. | [optional] 
**router_id** | **str** | Router id of the router - an unsigned 32-bit integer expressed in dotted quad notation. | [optional] 
**src_address** | **str** | Set the preferred source address when installing routes in the kernel. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_bgp_global import ConfigBgpGlobal

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigBgpGlobal from a JSON string
config_bgp_global_instance = ConfigBgpGlobal.from_json(json)
# print the JSON string representation of the object
print ConfigBgpGlobal.to_json()

# convert the object into a dict
config_bgp_global_dict = config_bgp_global_instance.to_dict()
# create an instance of ConfigBgpGlobal from a dict
config_bgp_global_form_dict = config_bgp_global.from_dict(config_bgp_global_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


