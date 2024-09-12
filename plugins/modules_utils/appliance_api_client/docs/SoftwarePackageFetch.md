# SoftwarePackageFetch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**fetch_id** | **str** |  | 
**status** | [**FetchStatus**](FetchStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.software_package_fetch import SoftwarePackageFetch

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackageFetch from a JSON string
software_package_fetch_instance = SoftwarePackageFetch.from_json(json)
# print the JSON string representation of the object
print SoftwarePackageFetch.to_json()

# convert the object into a dict
software_package_fetch_dict = software_package_fetch_instance.to_dict()
# create an instance of SoftwarePackageFetch from a dict
software_package_fetch_form_dict = software_package_fetch.from_dict(software_package_fetch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


