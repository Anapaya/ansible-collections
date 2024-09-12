# SoftwarePackageInstallInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**install_id** | **str** |  | 
**install_status** | [**InstallStatus**](InstallStatus.md) |  | [optional] 
**rollback_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.software_package_install_info import SoftwarePackageInstallInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackageInstallInfo from a JSON string
software_package_install_info_instance = SoftwarePackageInstallInfo.from_json(json)
# print the JSON string representation of the object
print SoftwarePackageInstallInfo.to_json()

# convert the object into a dict
software_package_install_info_dict = software_package_install_info_instance.to_dict()
# create an instance of SoftwarePackageInstallInfo from a dict
software_package_install_info_form_dict = software_package_install_info.from_dict(software_package_install_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


