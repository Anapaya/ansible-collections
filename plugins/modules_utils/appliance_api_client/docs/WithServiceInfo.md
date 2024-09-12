# WithServiceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from openapi_client.models.with_service_info import WithServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WithServiceInfo from a JSON string
with_service_info_instance = WithServiceInfo.from_json(json)
# print the JSON string representation of the object
print WithServiceInfo.to_json()

# convert the object into a dict
with_service_info_dict = with_service_info_instance.to_dict()
# create an instance of WithServiceInfo from a dict
with_service_info_form_dict = with_service_info.from_dict(with_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


