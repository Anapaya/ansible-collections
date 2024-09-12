# HealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | The identifier of the health check type. There can be multiple instances of the same health check in the response.  See the description of the &#x60;data&#x60; field for more information on how the health check is evaluated.  | 
**name** | **str** | The human readable name of the health check type. To identify the type of health check in automated systems, use the &#x60;id&#x60; field instead.  | 
**status** | [**HealthStatus**](HealthStatus.md) |  | 
**detail** | **str** | A human readable explanation of the health check status.  | [optional] 
**data** | [**DomainExchangesIPPrefixesData**](DomainExchangesIPPrefixesData.md) |  | 
**component** | [**HealthComponent**](HealthComponent.md) |  | 
**service_name** | **str** | Name of the service that the health check applies to. | 

## Example

```python
from openapi_client.models.health_check import HealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheck from a JSON string
health_check_instance = HealthCheck.from_json(json)
# print the JSON string representation of the object
print HealthCheck.to_json()

# convert the object into a dict
health_check_dict = health_check_instance.to_dict()
# create an instance of HealthCheck from a dict
health_check_form_dict = health_check.from_dict(health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


