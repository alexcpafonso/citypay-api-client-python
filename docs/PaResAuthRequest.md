# PaResAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md** | **str** | The Merchant Data (MD) which is a unique ID to reference the authentication session.  This value will be created by CityPay when required. When responding from the ACS, this value will be returned by the ACS.  | 
**pares** | **str** | The Payer Authentication Response packet which is returned by the ACS containing the  response of the authentication session including verification values. The response  is a base64 encoded packet and should be forwarded to CityPay untouched.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


