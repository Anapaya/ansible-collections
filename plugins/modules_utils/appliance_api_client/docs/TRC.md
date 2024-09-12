# TRC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**TRCID**](TRCID.md) |  | 
**validity** | [**Validity**](Validity.md) |  | 
**core_ases** | **List[str]** |  | 
**authoritative_ases** | **List[str]** |  | 
**description** | **str** |  | 
**blob** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.trc import TRC

# TODO update the JSON string below
json = "{}"
# create an instance of TRC from a JSON string
trc_instance = TRC.from_json(json)
# print the JSON string representation of the object
print TRC.to_json()

# convert the object into a dict
trc_dict = trc_instance.to_dict()
# create an instance of TRC from a dict
trc_form_dict = trc.from_dict(trc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


