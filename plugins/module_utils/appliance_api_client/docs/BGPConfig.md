# BGPConfig

BGP configuration the host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | The local AS number used for the BGP sessions. | 
**router_id** | **str** | The router ID used for the BGP sessions. | 
**neighbors** | [**List[BGPNeighbor]**](BGPNeighbor.md) | The BGP neighbors. | 
**networks** | **List[str]** | The prefixes in CIDR format that are advertised in the BGP sessions. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.bgp_config import BGPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BGPConfig from a JSON string
bgp_config_instance = BGPConfig.from_json(json)
# print the JSON string representation of the object
print BGPConfig.to_json()

# convert the object into a dict
bgp_config_dict = bgp_config_instance.to_dict()
# create an instance of BGPConfig from a dict
bgp_config_form_dict = bgp_config.from_dict(bgp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


