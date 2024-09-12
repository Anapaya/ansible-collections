# ConfigInterfacesEthernetRoute

List of routes belonging to this interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional human-readable string to comment on this route. | [optional] 
**var_from** | **str** | The source IP address for traffic going through the route. | [optional] 
**metric** | **int** | The metric for the route. The lower its value, the higher its priority. | [optional] [default to 0]
**sequence_id** | **int** | The sequence id determines the order of the route entries. | 
**to** | **str** | The destination prefix in CIDR notation of this route. | 
**via** | **str** | The next hop address which should be used for the prefix. | 

## Example

```python
from openapi_client.models.config_interfaces_ethernet_route import ConfigInterfacesEthernetRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesEthernetRoute from a JSON string
config_interfaces_ethernet_route_instance = ConfigInterfacesEthernetRoute.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesEthernetRoute.to_json()

# convert the object into a dict
config_interfaces_ethernet_route_dict = config_interfaces_ethernet_route_instance.to_dict()
# create an instance of ConfigInterfacesEthernetRoute from a dict
config_interfaces_ethernet_route_form_dict = config_interfaces_ethernet_route.from_dict(config_interfaces_ethernet_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


