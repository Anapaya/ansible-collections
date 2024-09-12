# ConfigManagementTelemetryLabels

List of labels which are attached to telemetry data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Name of the label. | [optional] 
**value** | **str** | Value of the label. | [optional] 

## Example

```python
from openapi_client.models.config_management_telemetry_labels import ConfigManagementTelemetryLabels

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigManagementTelemetryLabels from a JSON string
config_management_telemetry_labels_instance = ConfigManagementTelemetryLabels.from_json(json)
# print the JSON string representation of the object
print ConfigManagementTelemetryLabels.to_json()

# convert the object into a dict
config_management_telemetry_labels_dict = config_management_telemetry_labels_instance.to_dict()
# create an instance of ConfigManagementTelemetryLabels from a dict
config_management_telemetry_labels_form_dict = config_management_telemetry_labels.from_dict(config_management_telemetry_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


