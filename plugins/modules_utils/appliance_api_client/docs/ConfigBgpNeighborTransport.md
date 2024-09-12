# ConfigBgpNeighborTransport

Transport session parameters for the BGP neighbor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_address** | **str** | Set the local IPv4 address to be used for the session when sending BGP update messages. This may be expressed as either an IP address or the name of an interface. | [optional] 

## Example

```python
from openapi_client.models.config_bgp_neighbor_transport import ConfigBgpNeighborTransport

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigBgpNeighborTransport from a JSON string
config_bgp_neighbor_transport_instance = ConfigBgpNeighborTransport.from_json(json)
# print the JSON string representation of the object
print ConfigBgpNeighborTransport.to_json()

# convert the object into a dict
config_bgp_neighbor_transport_dict = config_bgp_neighbor_transport_instance.to_dict()
# create an instance of ConfigBgpNeighborTransport from a dict
config_bgp_neighbor_transport_form_dict = config_bgp_neighbor_transport.from_dict(config_bgp_neighbor_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


