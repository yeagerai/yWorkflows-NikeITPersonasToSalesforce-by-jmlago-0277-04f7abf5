
# NikeITPersonasToSalesforce

The NikeITPersonasToSalesforce workflow is responsible for pushing Nike IT personas data into Salesforce. It takes Salesforce credentials as input and pushes the data to Salesforce. After successfully pushing the data, it returns a boolean value 'success' and a list of created record ID.

## Initial generation prompt
description: "IOs - inputs:\n  SalesforceCredentials:\n    organization_id: string\n\
  \    password: string\n    security_token: string\n    username: string\noutputs:\n\
  \  DataPushedToSalesforce:\n    created_records: List[int]\n    success: bool\n"
name: NikeITPersonasToSalesforce


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        