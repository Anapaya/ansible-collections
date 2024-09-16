# ConfigBgpNeighborBfd

BFD configuration parameters relating to the BGP neighbor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_minimum_tx_interval** | **int** | Minimum desired control packet transmission interval in milliseconds | [optional] [default to 300]
**detection_multiplier** | **int** | Local session detection multiplier | [optional] [default to 3]
**enabled** | **bool** | Enable BFD for the BGP neighbor | [optional] [default to False]
**local_address** | **str** | Local address to use for BFD | [optional] 
**minimum_ttl** | **int** | For multihop sessions only: configure the minimum expected TTL for an incoming BFD control packet. | [optional] [default to 254]
**multihop** | **bool** | Enable BFD multihop | [optional] [default to False]
**required_minimum_receive** | **int** | Minimum required control packet receive interval in milliseconds | [optional] [default to 300]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_bgp_neighbor_bfd import ConfigBgpNeighborBfd

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigBgpNeighborBfd from a JSON string
config_bgp_neighbor_bfd_instance = ConfigBgpNeighborBfd.from_json(json)
# print the JSON string representation of the object
print ConfigBgpNeighborBfd.to_json()

# convert the object into a dict
config_bgp_neighbor_bfd_dict = config_bgp_neighbor_bfd_instance.to_dict()
# create an instance of ConfigBgpNeighborBfd from a dict
config_bgp_neighbor_bfd_form_dict = config_bgp_neighbor_bfd.from_dict(config_bgp_neighbor_bfd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


