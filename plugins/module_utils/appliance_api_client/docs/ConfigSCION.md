# ConfigSCION

Top-level configuration and state for the SCION protocol.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ases** | [**List[ConfigSCIONAS]**](ConfigSCIONAS.md) | List of SCION ASes that this device is part of identified by their ISD-AS identifier. | [optional] 
**synchronization** | [**ConfigSCIONSynchronization**](ConfigSCIONSynchronization.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion import ConfigSCION

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCION from a JSON string
config_scion_instance = ConfigSCION.from_json(json)
# print the JSON string representation of the object
print ConfigSCION.to_json()

# convert the object into a dict
config_scion_dict = config_scion_instance.to_dict()
# create an instance of ConfigSCION from a dict
config_scion_form_dict = config_scion.from_dict(config_scion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


