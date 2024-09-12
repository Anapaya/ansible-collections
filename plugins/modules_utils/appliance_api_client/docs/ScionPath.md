# ScionPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | The fingerprint of the path. | 
**human** | **str** | Human readable representation of the SCION path. | 
**hops** | [**List[ScionPathHop]**](ScionPathHop.md) | List of individual hops on the SCION path. | 
**status** | **str** | Human readable description of the state of the path. | 
**next_hop** | **str** | Next hop is the address of the local SCION router to use. | 
**expiration** | **datetime** | Expiry specifies until when is the path valid. | 
**mtu** | **int** | MTU of the path. | 

## Example

```python
from openapi_client.models.scion_path import ScionPath

# TODO update the JSON string below
json = "{}"
# create an instance of ScionPath from a JSON string
scion_path_instance = ScionPath.from_json(json)
# print the JSON string representation of the object
print ScionPath.to_json()

# convert the object into a dict
scion_path_dict = scion_path_instance.to_dict()
# create an instance of ScionPath from a dict
scion_path_form_dict = scion_path.from_dict(scion_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


