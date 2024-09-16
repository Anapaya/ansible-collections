# ConfigNatSnat

Top-level configuration and state for the source NAT.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_pool** | **List[str]** | The list of IP prefixes to use as the source NAT pool. | [optional] 
**exclude** | **List[str]** | The list of IP prefixes to exclude from the NAT. The number of IP addresses that can be excluded is limited. | [optional] 
**interfaces** | **List[str]** | The list of interfaces to do the NAT. These are typically interfaces connected to the local network | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_nat_snat import ConfigNatSnat

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigNatSnat from a JSON string
config_nat_snat_instance = ConfigNatSnat.from_json(json)
# print the JSON string representation of the object
print ConfigNatSnat.to_json()

# convert the object into a dict
config_nat_snat_dict = config_nat_snat_instance.to_dict()
# create an instance of ConfigNatSnat from a dict
config_nat_snat_form_dict = config_nat_snat.from_dict(config_nat_snat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


