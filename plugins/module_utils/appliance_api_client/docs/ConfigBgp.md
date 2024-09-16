# ConfigBgp

Top-level configuration and state for the BGP router.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | [**ConfigBgpGlobal**](ConfigBgpGlobal.md) |  | [optional] 
**neighbors** | [**List[ConfigBgpNeighbor]**](ConfigBgpNeighbor.md) | Configuration for BGP neighbors | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_bgp import ConfigBgp

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigBgp from a JSON string
config_bgp_instance = ConfigBgp.from_json(json)
# print the JSON string representation of the object
print ConfigBgp.to_json()

# convert the object into a dict
config_bgp_dict = config_bgp_instance.to_dict()
# create an instance of ConfigBgp from a dict
config_bgp_form_dict = config_bgp.from_dict(config_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


