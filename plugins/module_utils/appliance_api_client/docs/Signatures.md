# Signatures


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the signed file | 
**sha256sum** | **str** | SHA256 hash of the signed file | 
**signatures** | [**List[Signature]**](Signature.md) | A list of signatures | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.signatures import Signatures

# TODO update the JSON string below
json = "{}"
# create an instance of Signatures from a JSON string
signatures_instance = Signatures.from_json(json)
# print the JSON string representation of the object
print Signatures.to_json()

# convert the object into a dict
signatures_dict = signatures_instance.to_dict()
# create an instance of Signatures from a dict
signatures_form_dict = signatures.from_dict(signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


