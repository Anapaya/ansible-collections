# ConfigSystemKernel

Anapaya appliance Linux kernel configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hugepage_size** | **str** | Size of hugepages the kernel should allocate at boot time. | [optional] [default to '2M']
**hugepages** | **int** | Number of hugepages the kernel should allocate at boot time. If not set, a sensible default is used based on the available memory. | [optional] 
**iommu_enabled** | **bool** | Whether the IOMMU subsystem in the Linux kernel is enabled. IOMMU should be enabled on systems that support it for better performance. Note: After changing this option the appliance needs to be rebooted. | [optional] [default to False]

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_system_kernel import ConfigSystemKernel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSystemKernel from a JSON string
config_system_kernel_instance = ConfigSystemKernel.from_json(json)
# print the JSON string representation of the object
print ConfigSystemKernel.to_json()

# convert the object into a dict
config_system_kernel_dict = config_system_kernel_instance.to_dict()
# create an instance of ConfigSystemKernel from a dict
config_system_kernel_form_dict = config_system_kernel.from_dict(config_system_kernel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


