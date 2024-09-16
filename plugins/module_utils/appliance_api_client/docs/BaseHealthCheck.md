# BaseHealthCheck


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | The identifier of the health check type. There can be multiple instances of the same health check in the response.  See the description of the &#x60;data&#x60; field for more information on how the health check is evaluated.  | 
**name** | **str** | The human readable name of the health check type. To identify the type of health check in automated systems, use the &#x60;id&#x60; field instead.  | 
**status** | [**HealthStatus**](HealthStatus.md) |  | 
**detail** | **str** | A human readable explanation of the health check status.  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.base_health_check import BaseHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of BaseHealthCheck from a JSON string
base_health_check_instance = BaseHealthCheck.from_json(json)
# print the JSON string representation of the object
print BaseHealthCheck.to_json()

# convert the object into a dict
base_health_check_dict = base_health_check_instance.to_dict()
# create an instance of BaseHealthCheck from a dict
base_health_check_form_dict = base_health_check.from_dict(base_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


