# ConfigScionTunnelingDomainRemoteMatcher

List of remote matchers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specify the matchers action. | 
**description** | **str** | Description for the remote matcher. | [optional] 
**isd_as** | **str** | The ISD-AS identifier. The matcher matches the ISD-AS identifier of a SCION AS. 0 indicates a wildcard (both for ISD and AS). | 
**sequence_id** | **int** | The sequence ID determines the order in which sequence the remote matchers are applied. The sequence ID must be unique for each entry. Target devices apply the remote matchers in order of ascending sequence ID (low to high). | 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_domain_remote_matcher import ConfigScionTunnelingDomainRemoteMatcher

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingDomainRemoteMatcher from a JSON string
config_scion_tunneling_domain_remote_matcher_instance = ConfigScionTunnelingDomainRemoteMatcher.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingDomainRemoteMatcher.to_json()

# convert the object into a dict
config_scion_tunneling_domain_remote_matcher_dict = config_scion_tunneling_domain_remote_matcher_instance.to_dict()
# create an instance of ConfigScionTunnelingDomainRemoteMatcher from a dict
config_scion_tunneling_domain_remote_matcher_form_dict = config_scion_tunneling_domain_remote_matcher.from_dict(config_scion_tunneling_domain_remote_matcher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


