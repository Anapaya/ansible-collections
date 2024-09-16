# PackageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.package_info import PackageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PackageInfo from a JSON string
package_info_instance = PackageInfo.from_json(json)
# print the JSON string representation of the object
print PackageInfo.to_json()

# convert the object into a dict
package_info_dict = package_info_instance.to_dict()
# create an instance of PackageInfo from a dict
package_info_form_dict = package_info.from_dict(package_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


