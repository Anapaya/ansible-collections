# TRCID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isd** | **int** |  | 
**base_number** | **int** |  | 
**serial_number** | **int** |  | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trcid import TRCID

# TODO update the JSON string below
json = "{}"
# create an instance of TRCID from a JSON string
trcid_instance = TRCID.from_json(json)
# print the JSON string representation of the object
print TRCID.to_json()

# convert the object into a dict
trcid_dict = trcid_instance.to_dict()
# create an instance of TRCID from a dict
trcid_form_dict = trcid.from_dict(trcid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


