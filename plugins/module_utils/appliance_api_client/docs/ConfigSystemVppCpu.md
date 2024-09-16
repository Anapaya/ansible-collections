# ConfigSystemVppCpu

CPU configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corelist_workers** | **str** | The list of CPU cores to be used by the workers. The cores are pinned to the workers in the order they are listed. The format for the list is A,B1-Bn,C1-Cn. This setting is mutually exclusive with workers and the list must not contain the main-core. | [optional] 
**main_core** | **int** | The logical CPU core where main thread runs. | [optional] [default to 1]
**workers** | **int** | The number of workers to be created for VPP. The workers are pinned to consecutive CPU cores. If set to 0, packet processing is performed by the main-core | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_vpp_cpu import ConfigSystemVppCpu

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemVppCpu from a JSON string
config_system_vpp_cpu_instance = ConfigSystemVppCpu.from_json(json)
# print the JSON string representation of the object
print ConfigSystemVppCpu.to_json()

# convert the object into a dict
config_system_vpp_cpu_dict = config_system_vpp_cpu_instance.to_dict()
# create an instance of ConfigSystemVppCpu from a dict
config_system_vpp_cpu_form_dict = config_system_vpp_cpu.from_dict(config_system_vpp_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


