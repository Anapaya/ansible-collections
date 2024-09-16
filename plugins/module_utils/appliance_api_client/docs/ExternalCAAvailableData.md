# ExternalCAAvailableData

The external CA can be reached and is available. This check is only exposed if the SCION control service is configured to use an external CA for issuing new certificates. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the external CA.  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.external_ca_available_data import ExternalCAAvailableData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCAAvailableData from a JSON string
external_ca_available_data_instance = ExternalCAAvailableData.from_json(json)
# print the JSON string representation of the object
print ExternalCAAvailableData.to_json()

# convert the object into a dict
external_ca_available_data_dict = external_ca_available_data_instance.to_dict()
# create an instance of ExternalCAAvailableData from a dict
external_ca_available_data_form_dict = external_ca_available_data.from_dict(external_ca_available_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


