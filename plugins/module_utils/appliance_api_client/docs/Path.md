# Path


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprint** | **str** | Hex-string representing the paths fingerprint. | 
**hops** | [**List[Hop]**](Hop.md) |  | 
**next_hop** | **str** | The internal UDP/IP underlay address of the SCION router that forwards traffic for this path.  | 
**expiry** | **datetime** | Expiration time of the path. | 
**mtu** | **int** | The maximum transmission unit in bytes for SCION packets. This represents the protocol data unit (PDU) of the SCION layer on this path. | 
**latency** | **List[str]** | Optional array of latency measurements between any two consecutive interfaces. Entry i describes the latency between interface i and i+1.  | [optional] 
**status** | **str** |  | [optional] 
**local_ip** | **str** |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.path import Path

# TODO update the JSON string below
json = "{}"
# create an instance of Path from a JSON string
path_instance = Path.from_json(json)
# print the JSON string representation of the object
print Path.to_json()

# convert the object into a dict
path_dict = path_instance.to_dict()
# create an instance of Path from a dict
path_form_dict = path.from_dict(path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


