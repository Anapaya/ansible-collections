# Health


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | 
**checks** | [**List[Check]**](Check.md) | List of health checks. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.health import Health

# TODO update the JSON string below
json = "{}"
# create an instance of Health from a JSON string
health_instance = Health.from_json(json)
# print the JSON string representation of the object
print Health.to_json()

# convert the object into a dict
health_dict = health_instance.to_dict()
# create an instance of Health from a dict
health_form_dict = health.from_dict(health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


