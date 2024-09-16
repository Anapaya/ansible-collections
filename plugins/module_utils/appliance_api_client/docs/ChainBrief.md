# ChainBrief


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**subject** | **str** |  | 
**issuer** | **str** |  | 
**validity** | [**Validity**](Validity.md) |  | 
**chain** | **str** |  | [optional] 
**blob** | **str** |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.chain_brief import ChainBrief

# TODO update the JSON string below
json = "{}"
# create an instance of ChainBrief from a JSON string
chain_brief_instance = ChainBrief.from_json(json)
# print the JSON string representation of the object
print ChainBrief.to_json()

# convert the object into a dict
chain_brief_dict = chain_brief_instance.to_dict()
# create an instance of ChainBrief from a dict
chain_brief_form_dict = chain_brief.from_dict(chain_brief_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


