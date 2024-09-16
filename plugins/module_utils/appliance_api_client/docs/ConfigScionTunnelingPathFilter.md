# ConfigScionTunnelingPathFilter

List of path filters. A path filter filters the set of paths that can be used for IP-in-SCION tunneling. The filter must include an ACL and/or a hop pattern. A path is included if it is accepted by both the ACL and the hop pattern (if specified).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **List[str]** | The ACL that is applied on the path. An ACL consists of a list of ACL entries. Each ACL entry has the form &#x60;action hop-predicate&#x60;, where the action can either be accept (+) or deny (-). The hop predicate is optional and has the form &#x60;isd-as#interface&#x60;, where &#x60;isd&#x60; is the ISD identifier, &#x60;as&#x60; is the AS identifier, and &#x60;interface&#x60; is the interface identifier of a SCION path hop. The hop predicate can be fully or partially qualified, i.e., all entries of the hop predicate are optional or can include wildcards (0). If no hop predicate is specified the action matches every hop, i.e., a single &#39;+&#39; is the default accept action and a single &#39;-&#39; is the default deny action. The ACL is applied by sequentially applying all ACL entries to paths. If the ACL is empty, it defaults to accepting all paths. | [optional] 
**description** | **str** | Description, or comment, for the path filter. | [optional] 
**hop_pattern** | **str** | The sequence of hop predicates that a path has to match to be accepted. Each hop predicate can optionally be extended with a modifier &#39;*&#39; or &#39;+&#39;. The &#39;*&#39; modifier means 0 or more occurrences. The &#39;+&#39; means one or more occurrences. | [optional] 
**name** | **str** | Name of the path filter. This is value is used by the path policy to reference the path filter. | [optional] 

## Example

```python
from ansible.module_utils.appliance_api_client.models.config_scion_tunneling_path_filter import ConfigScionTunnelingPathFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigScionTunnelingPathFilter from a JSON string
config_scion_tunneling_path_filter_instance = ConfigScionTunnelingPathFilter.from_json(json)
# print the JSON string representation of the object
print ConfigScionTunnelingPathFilter.to_json()

# convert the object into a dict
config_scion_tunneling_path_filter_dict = config_scion_tunneling_path_filter_instance.to_dict()
# create an instance of ConfigScionTunnelingPathFilter from a dict
config_scion_tunneling_path_filter_form_dict = config_scion_tunneling_path_filter.from_dict(config_scion_tunneling_path_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


