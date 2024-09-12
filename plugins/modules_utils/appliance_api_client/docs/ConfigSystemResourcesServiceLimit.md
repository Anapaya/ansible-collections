# ConfigSystemResourcesServiceLimit

Per service resource limits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **float** | The CPU limit in number of fractional CPU cores that can be used by the service. If not specified, a sensible default is chosen by the system. If set to 0, the service is not limited in terms of CPU usage. | [optional] 
**memory** | **str** | The memory limit in bytes that can be used by the service. The limit can be specified using a string of the format &lt;decimal&gt;&lt;suffix&gt;, where suffix can either be empty or one of &#39;K&#39;, &#39;k&#39;, &#39;M&#39;, &#39;m&#39;, &#39;G&#39;, &#39;g&#39; or &#39;T&#39;, &#39;t&#39;. Note that the step between the suffixes is 1024. If not specified, a sensible default is chosen by the system. If set to 0, the service is not limited in terms of memory usage. The minimum value is 6M. | [optional] 
**name** | **str** | Name of the service. | 

## Example

```python
from openapi_client.models.config_system_resources_service_limit import ConfigSystemResourcesServiceLimit

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemResourcesServiceLimit from a JSON string
config_system_resources_service_limit_instance = ConfigSystemResourcesServiceLimit.from_json(json)
# print the JSON string representation of the object
print ConfigSystemResourcesServiceLimit.to_json()

# convert the object into a dict
config_system_resources_service_limit_dict = config_system_resources_service_limit_instance.to_dict()
# create an instance of ConfigSystemResourcesServiceLimit from a dict
config_system_resources_service_limit_form_dict = config_system_resources_service_limit.from_dict(config_system_resources_service_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


