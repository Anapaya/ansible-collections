# ConfigSCIONASDetails

User-defined details about the SCION AS for informational purpose.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | User-defined description, or comment, that describes this SCION AS. | [optional] 
**name** | **str** | SCION AS name for informational purpose. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas_details import ConfigSCIONASDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONASDetails from a JSON string
config_scionas_details_instance = ConfigSCIONASDetails.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONASDetails.to_json()

# convert the object into a dict
config_scionas_details_dict = config_scionas_details_instance.to_dict()
# create an instance of ConfigSCIONASDetails from a dict
config_scionas_details_form_dict = config_scionas_details.from_dict(config_scionas_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


