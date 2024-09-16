# MetaHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.meta_health_check import MetaHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of MetaHealthCheck from a JSON string
meta_health_check_instance = MetaHealthCheck.from_json(json)
# print the JSON string representation of the object
print MetaHealthCheck.to_json()

# convert the object into a dict
meta_health_check_dict = meta_health_check_instance.to_dict()
# create an instance of MetaHealthCheck from a dict
meta_health_check_form_dict = meta_health_check.from_dict(meta_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


