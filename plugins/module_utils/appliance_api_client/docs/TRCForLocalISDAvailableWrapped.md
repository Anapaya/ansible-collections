# TRCForLocalISDAvailableWrapped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trc_for_local_isd_available_wrapped import TRCForLocalISDAvailableWrapped

# TODO update the JSON string below
json = "{}"
# create an instance of TRCForLocalISDAvailableWrapped from a JSON string
trc_for_local_isd_available_wrapped_instance = TRCForLocalISDAvailableWrapped.from_json(json)
# print the JSON string representation of the object
print TRCForLocalISDAvailableWrapped.to_json()

# convert the object into a dict
trc_for_local_isd_available_wrapped_dict = trc_for_local_isd_available_wrapped_instance.to_dict()
# create an instance of TRCForLocalISDAvailableWrapped from a dict
trc_for_local_isd_available_wrapped_form_dict = trc_for_local_isd_available_wrapped.from_dict(trc_for_local_isd_available_wrapped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


