# ScionTunnelingRoutingChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routing_chain_id** | **str** | Unique ID of the routing chain. | 
**routing_chain_id_legacy** | **int** | Unique ID of the routing chain. | 
**prefixes** | **List[str]** | A list of IP prefixes handled by this routing chain. | 
**domain** | **str** | The domain this routing chain is used to access. | 
**traffic_matchers** | [**List[ScionTunnelingTrafficMatcher]**](ScionTunnelingTrafficMatcher.md) | A list of different classes of IP packets handled by this routing chain. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.scion_tunneling_routing_chain import ScionTunnelingRoutingChain

# TODO update the JSON string below
json = "{}"
# create an instance of ScionTunnelingRoutingChain from a JSON string
scion_tunneling_routing_chain_instance = ScionTunnelingRoutingChain.from_json(json)
# print the JSON string representation of the object
print ScionTunnelingRoutingChain.to_json()

# convert the object into a dict
scion_tunneling_routing_chain_dict = scion_tunneling_routing_chain_instance.to_dict()
# create an instance of ScionTunnelingRoutingChain from a dict
scion_tunneling_routing_chain_form_dict = scion_tunneling_routing_chain.from_dict(scion_tunneling_routing_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


