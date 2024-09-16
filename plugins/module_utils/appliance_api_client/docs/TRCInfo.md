# TRCInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The TRC identifier composed of the ISD identfier, base and serial number. | 
**isd** | **int** | The ISD of the TRC. | 
**base** | **int** | The base number of the TRC. Usually 1, unless a trust reset has been performed. | 
**serial** | **int** | The serial number of the TRC. Incremented with each new TRC. | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.trc_info import TRCInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TRCInfo from a JSON string
trc_info_instance = TRCInfo.from_json(json)
# print the JSON string representation of the object
print TRCInfo.to_json()

# convert the object into a dict
trc_info_dict = trc_info_instance.to_dict()
# create an instance of TRCInfo from a dict
trc_info_form_dict = trc_info.from_dict(trc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


