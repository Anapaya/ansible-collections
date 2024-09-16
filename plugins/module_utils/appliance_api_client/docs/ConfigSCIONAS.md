# ConfigSCIONAS

SCION AS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_service** | [**ConfigSCIONASCAService**](ConfigSCIONASCAService.md) |  | [optional] 
**control** | [**ConfigSCIONASControl**](ConfigSCIONASControl.md) |  | [optional] 
**core** | **bool** | Indicate whether the AS is core in its ISD. A SCION core AS must only have other core ASes or child ASes as neighbors. A SCION non-core AS must only have parent. child, or peer ASes as neighbors. | [optional] 
**cppki** | [**ConfigSCIONASCPPKI**](ConfigSCIONASCPPKI.md) |  | [optional] 
**default** | **bool** | Default indicates whether the respective SCION AS should be used by default as the source AS by SCION applications, e.g., scion ping or scion showpaths. The configurations with more than one default ASes will be rejected because there can only be one default AS. If there is only a single AS configured, it will be the default. Therefore, this setting is only necessary if multiple ASes are configured on the appliance. | [optional] [default to False]
**details** | [**ConfigSCIONASDetails**](ConfigSCIONASDetails.md) |  | [optional] 
**forwarding_key** | **str** | The forwarding key for this AS. Note that changing this key might result in a network disruption and it is therefore not recommended. | [optional] 
**isd_as** | **str** | ISD-AS identifier of the SCION AS. | 
**neighbors** | [**List[ConfigSCIONASNeighbor]**](ConfigSCIONASNeighbor.md) | List of neighbor SCION ASes that this device is connected to via one or multiple SCION interfaces. Each entry is identified by the remote ISD-AS. | [optional] 
**router** | [**ConfigSCIONASRouter**](ConfigSCIONASRouter.md) |  | [optional] 
**scion_mtu** | **int** | The maximum transmission unit in bytes for SCION packets. This represents the protocol data unit (PDU) of the SCION layer on this interface and is usually calculated as maximum Ethernet payload - IP Header - UDP Header.  | [optional] [default to 1472]
**shard_id** | **int** | The control and the data plane of a SCION AS is split into multiple shards. Each shard is responsible for processing and disseminating pathing information only for a subset of links. This field is the ID of the shard to which the control service and the router on this appliance belong. It is recommended to have the router and the control service from the same shard on the same host and if they are not then the routers and the control service in the same shard need mutual IP connectivity. Each shard must contain only a single control service. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scionas import ConfigSCIONAS

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSCIONAS from a JSON string
config_scionas_instance = ConfigSCIONAS.from_json(json)
# print the JSON string representation of the object
print ConfigSCIONAS.to_json()

# convert the object into a dict
config_scionas_dict = config_scionas_instance.to_dict()
# create an instance of ConfigSCIONAS from a dict
config_scionas_form_dict = config_scionas.from_dict(config_scionas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


