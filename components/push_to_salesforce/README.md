
# PushToSalesforce

Pushes the given data into Salesforce, mapping the 'employees_data' output from the ScrapeNikeITPersonas component to 'contacts_data'. Takes the input from another node: 'contacts_data', along with the input 'SalesforceCredentials', and outputs 'created_records' as a list of integers and 'success' as a boolean.

## Initial generation prompt
description: 'Pushes the given data into Salesforce, mapping the ''employees_data''
  output from the ScrapeNikeITPersonas component to ''contacts_data''. Takes the input
  from another node: ''contacts_data'', along with the input ''SalesforceCredentials'',
  and outputs ''created_records'' as a list of integers and ''success'' as a boolean.'
name: PushToSalesforce


## Transformer breakdown
- 1. Authenticate with Salesforce API using SalesforceCredentials.
- 2. Map the 'employees_data' from the ScrapeNikeITPersonas component to 'contacts_data'.
- 3. Begin looping through each contact in the 'contacts_data' list.
- 4. Push the contact to Salesforce.
- 5. Add the returned record ID to the 'created_records' list.
- 6. If all contacts have been pushed to Salesforce, set 'success' to True, else False.

## Parameters
[]

        