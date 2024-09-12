# ConfigScionTunnelingDomainPrefixesAcceptFilterEntry

List of prefix matchers. Prefixes that are announced by remotes are filtered by the prefix matchers in order by accepting all IPs that are in _accepted_ matchers and rejecting ones that are in _rejected_ prefix matchers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specify matchers action. | 
**description** | **str** | Optional description for the prefix matcher. | [optional] 
**prefixes** | **List[str]** | The list of IP prefixes used for matching. The matcher matches all IP prefixes that are contained in the union of the specified IP prefixes, i.e. it matches all listed prefixes as well as their contained more specific prefixes. | [optional] 
**sequence_id** | **int** | The sequence ID determines the order in which sequence the prefix matchers are applied. The sequence ID must be unique for each entry. Target devices apply the prefix matchers in order of ascending sequence ID (low to high) accepting all IPs that are in _accepted_ matchers and rejecting the ones that are in _rejected_ matchers. | 

## Example

```python
from openapi_client.models.config_scion_tunneling_domain_prefixes_accept_filter_entry import ConfigScionTunnelingDomainPrefixesAcceptFilterEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingDomainPrefixesAcceptFilterEntry from a JSON string
config_scion_tunneling_domain_prefixes_accept_filter_entry_instance = ConfigScionTunnelingDomainPrefixesAcceptFilterEntry.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingDomainPrefixesAcceptFilterEntry.to_json()

# convert the object into a dict
config_scion_tunneling_domain_prefixes_accept_filter_entry_dict = config_scion_tunneling_domain_prefixes_accept_filter_entry_instance.to_dict()
# create an instance of ConfigScionTunnelingDomainPrefixesAcceptFilterEntry from a dict
config_scion_tunneling_domain_prefixes_accept_filter_entry_form_dict = config_scion_tunneling_domain_prefixes_accept_filter_entry.from_dict(config_scion_tunneling_domain_prefixes_accept_filter_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


