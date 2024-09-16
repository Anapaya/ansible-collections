# ConfigNat

Top-level configuration and state for NAT.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snat** | [**ConfigNatSnat**](ConfigNatSnat.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_nat import ConfigNat

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigNat from a JSON string
config_nat_instance = ConfigNat.from_json(json)
# print the JSON string representation of the object
print ConfigNat.to_json()

# convert the object into a dict
config_nat_dict = config_nat_instance.to_dict()
# create an instance of ConfigNat from a dict
config_nat_form_dict = config_nat.from_dict(config_nat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


