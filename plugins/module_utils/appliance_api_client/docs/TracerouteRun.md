# TracerouteRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_host** | **str** | IPv4 or IPv6 address | 
**destination_isd_as** | **str** |  | 
**source_isd_as** | **str** | If source_isd_as is unset, then the default ISD-AS from the configuration is used. | [optional] 
**sequence** | **str** | SCION paths can be filtered according to a sequence. A sequence is a string of space separated HopPredicates. A Hop Predicate (HP) is of the form &#39;ISD-AS#IF,IF&#39;. The first IF means the inbound interface (the interface where packet enters the AS) and the second IF means the outbound interface (the interface where packet leaves the AS). 0 can be used as a wildcard for ISD, AS and both IF elements independently.  HopPredicate Examples:    - Match any:                               0   - Match ISD 1:                             1   - Match AS 1-ff00:0:133:                   1-ff00:0:133   - Match IF 2 of AS 1-ff00:0:133:           1-ff00:0:133#2   - Match inbound IF 2 of AS 1-ff00:0:133:   1-ff00:0:133#2,0   - Match outbound IF 2 of AS 1-ff00:0:133:  1-ff00:0:133#0,2  Sequence Examples:  &#x60;&#x60;&#x60; sequence: \&quot;1-ff00:0:133#0 1-ff00:0:120#2,1 0 0 1-ff00:0:110#0\&quot; &#x60;&#x60;&#x60;  The above example specifies a path from any interface in AS 1-ff00:0:133 to two subsequent interfaces in AS 1-ff00:0:120 (entering on interface 2 and exiting on interface 1), then there are two wildcards that each match any AS. The path must end with any interface in AS 1-ff00:0:110. &#x60;&#x60;&#x60;   sequence: \&quot;1-ff00:0:133#1 1+ 2-ff00:0:1? 2-ff00:0:233#1\&quot; &#x60;&#x60;&#x60; The above example includes operators and specifies a path from interface 1-ff00:0:133#1 through multiple ASes in ISD 1, that may (but does not need to) traverse AS 2-ff00:0:1 and then reaches its destination on 2-ff00:0:233#1. Available operators:    - ? (the preceding HopPredicate may appear at most once)   - \\+ (the preceding ISD-level HopPredicate must appear at least once)   - \\* (the preceding ISD-level HopPredicate may appear zero or more times)   - | (logical OR)  | [optional] 
**timeout** | **str** | Timeout per packet. Valid time units are \&quot;ms\&quot;, \&quot;s\&quot;. | [optional] [default to '1s']
**probes_per_hop** | **int** | Number of probes per hop | [optional] [default to 3]

## Example

```python
from ansible.module_utils.appliance_api_client.models.traceroute_run import TracerouteRun

# TODO update the JSON string below
json = "{}"
# create an instance of TracerouteRun from a JSON string
traceroute_run_instance = TracerouteRun.from_json(json)
# print the JSON string representation of the object
print TracerouteRun.to_json()

# convert the object into a dict
traceroute_run_dict = traceroute_run_instance.to_dict()
# create an instance of TracerouteRun from a dict
traceroute_run_form_dict = traceroute_run.from_dict(traceroute_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


