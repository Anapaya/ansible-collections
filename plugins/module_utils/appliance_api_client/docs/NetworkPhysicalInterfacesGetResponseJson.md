# NetworkPhysicalInterfacesGetResponseJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interfaces** | [**List[PhysicalInterface]**](PhysicalInterface.md) | List of physical interfaces | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.network_physical_interfaces_get_response_json import NetworkPhysicalInterfacesGetResponseJson

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPhysicalInterfacesGetResponseJson from a JSON string
network_physical_interfaces_get_response_json_instance = NetworkPhysicalInterfacesGetResponseJson.from_json(json)
# print the JSON string representation of the object
print NetworkPhysicalInterfacesGetResponseJson.to_json()

# convert the object into a dict
network_physical_interfaces_get_response_json_dict = network_physical_interfaces_get_response_json_instance.to_dict()
# create an instance of NetworkPhysicalInterfacesGetResponseJson from a dict
network_physical_interfaces_get_response_json_form_dict = network_physical_interfaces_get_response_json.from_dict(network_physical_interfaces_get_response_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


