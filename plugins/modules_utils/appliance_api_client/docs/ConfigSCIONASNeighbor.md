# ConfigSCIONASNeighbor

Neighbor SCION AS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description, or comment, for the neighbor AS. | [optional] 
**interfaces** | [**List[ConfigSCIONASNeighborInterface]**](ConfigSCIONASNeighborInterface.md) | SCION interfaces on this device that link to the neighbor AS. | [optional] 
**neighbor_isd_as** | **str** | ISD-AS number of the neighbor AS. | 
**relationship** | **str** | The relationship to the neighbor AS. If the local AS is core, this value must either be CORE or CHILD. If the local is non-core, this value must either be PARENT, CHILD or PEER. | 

## Example

```python
from openapi_client.models.config_scionas_neighbor import ConfigSCIONASNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASNeighbor from a JSON string
config_scionas_neighbor_instance = ConfigSCIONASNeighbor.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASNeighbor.to_json()

# convert the object into a dict
config_scionas_neighbor_dict = config_scionas_neighbor_instance.to_dict()
# create an instance of ConfigSCIONASNeighbor from a dict
config_scionas_neighbor_form_dict = config_scionas_neighbor.from_dict(config_scionas_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


