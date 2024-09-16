# ConfigSystemVppBuffers

Buffers configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_size** | **int** | The size of VPP internal buffers, in bytes. | [optional] [default to 9000]
**num_buffers** | **int** | The number of VPP internal buffers. If set to 0, a 3/4 of the available hugepages are used for buffers. | [optional] [default to 0]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_vpp_buffers import ConfigSystemVppBuffers

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemVppBuffers from a JSON string
config_system_vpp_buffers_instance = ConfigSystemVppBuffers.from_json(json)
# print the JSON string representation of the object
print ConfigSystemVppBuffers.to_json()

# convert the object into a dict
config_system_vpp_buffers_dict = config_system_vpp_buffers_instance.to_dict()
# create an instance of ConfigSystemVppBuffers from a dict
config_system_vpp_buffers_form_dict = config_system_vpp_buffers.from_dict(config_system_vpp_buffers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


