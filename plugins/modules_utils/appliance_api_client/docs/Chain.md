# Chain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_certificate** | [**Certificate**](Certificate.md) |  | 
**ca_certificate** | [**Certificate**](Certificate.md) |  | 

## Example

```python
from openapi_client.models.chain import Chain

# TODO update the JSON string below
json = "{}"
# create an instance of Chain from a JSON string
chain_instance = Chain.from_json(json)
# print the JSON string representation of the object
print Chain.to_json()

# convert the object into a dict
chain_dict = chain_instance.to_dict()
# create an instance of Chain from a dict
chain_form_dict = chain.from_dict(chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


