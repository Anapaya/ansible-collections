# ExternalCAAvailable

Check data for an explanation of this health check. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExternalCAAvailableData**](ExternalCAAvailableData.md) |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.external_ca_available import ExternalCAAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCAAvailable from a JSON string
external_ca_available_instance = ExternalCAAvailable.from_json(json)
# print the JSON string representation of the object
print ExternalCAAvailable.to_json()

# convert the object into a dict
external_ca_available_dict = external_ca_available_instance.to_dict()
# create an instance of ExternalCAAvailable from a dict
external_ca_available_form_dict = external_ca_available.from_dict(external_ca_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


