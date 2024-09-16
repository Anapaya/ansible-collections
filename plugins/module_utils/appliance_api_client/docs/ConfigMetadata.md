# ConfigMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_version** | **str** | The version of the SCION package installed on the appliance. | 
**system_version** | **str** | The version of the system package installed on the appliance. If the value cannot be returned, the version will be marked as \&quot;unknown\&quot;. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_metadata import ConfigMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMetadata from a JSON string
config_metadata_instance = ConfigMetadata.from_json(json)
# print the JSON string representation of the object
print ConfigMetadata.to_json()

# convert the object into a dict
config_metadata_dict = config_metadata_instance.to_dict()
# create an instance of ConfigMetadata from a dict
config_metadata_form_dict = config_metadata.from_dict(config_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


