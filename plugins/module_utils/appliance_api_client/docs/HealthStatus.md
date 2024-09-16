# HealthStatus

The health status of the service. The status has several severity levels:  - `passing`: The service is healthy and operational. - `notice`: The service is healthy and operational, but there is something   that looks suspicious. E.g., an empty allow list. - `degraded`: The service is operational, but not all features are working   as expected. E.g., beaconing on a single link fails. - `failing`: The service is not operational.  See the description of the `data` field for more information on how the health check is evaluated. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


