# ConfigInterfacesBondRoute

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
from ansible.module_utils.appliance_api_client.models.config_interfaces_bond_route import ConfigInterfacesBondRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigInterfacesBondRoute from a JSON string
config_interfaces_bond_route_instance = ConfigInterfacesBondRoute.from_json(json)
# print the JSON string representation of the object
print ConfigInterfacesBondRoute.to_json()

# convert the object into a dict
config_interfaces_bond_route_dict = config_interfaces_bond_route_instance.to_dict()
# create an instance of ConfigInterfacesBondRoute from a dict
config_interfaces_bond_route_form_dict = config_interfaces_bond_route.from_dict(config_interfaces_bond_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


