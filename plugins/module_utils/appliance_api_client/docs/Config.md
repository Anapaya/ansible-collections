# Config

Anapaya appliance configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced** | [**ConfigAdvanced**](ConfigAdvanced.md) |  | [optional] 
**bgp** | [**ConfigBgp**](ConfigBgp.md) |  | [optional] 
**cluster** | [**ConfigCluster**](ConfigCluster.md) |  | [optional] 
**experiments** | [**ConfigExperiments**](ConfigExperiments.md) |  | [optional] 
**firewall** | [**ConfigFirewall**](ConfigFirewall.md) |  | [optional] 
**interfaces** | [**ConfigInterfaces**](ConfigInterfaces.md) |  | [optional] 
**management** | [**ConfigManagement**](ConfigManagement.md) |  | [optional] 
**nat** | [**ConfigNat**](ConfigNat.md) |  | [optional] 
**scion** | [**ConfigSCION**](ConfigSCION.md) |  | [optional] 
**scion_tunneling** | [**ConfigScionTunneling**](ConfigScionTunneling.md) |  | [optional] 
**system** | [**ConfigSystem**](ConfigSystem.md) |  | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print Config.to_json()

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_form_dict = config.from_dict(config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


