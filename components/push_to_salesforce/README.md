markdown
# Component Name: PushToSalesforce

## Description

This Yeager component is designed to push contact information to Salesforce. The component receives a list of contacts with their metadata and Salesforce credentials as inputs, and then it creates new contact records in Salesforce using the Simple Salesforce library. It returns a list of created records' IDs and a boolean flag indicating whether the operation was successful.

## Input and Output Models

The component relies on two Pydantic models to validate and serialize input and output data:

1. **PushToSalesforceInputDict**: This models the input data, which consists of the following fields:
    - `contacts_data` (List[Dict]): A list of contact records, where each record is a dictionary containing contact details (e.g., first_name, last_name, email, and phone).
    - `SalesforceCredentials` (Dict): A dictionary holding the Salesforce credentials required for authentication (e.g., username, password, and security_token).

2. **PushToSalesforceOutputDict**: This models the output data and includes the following fields:
    - `created_records` (List[int]): A list of created records' IDs in Salesforce.
    - `success` (bool): A boolean flag indicating whether the contact creation process was successful.

## Parameters

The PushToSalesforce component uses the following parameters:

- `args`: An instance of the PushToSalesforceInputDict model.

## Transform Function

The `transform()` method in the component performs the following steps:

1. Extract Salesforce credentials and contact data from the input argument.
2. Create a Salesforce instance using the extracted credentials.
3. Initialize an empty list to store created records' IDs.
4. Set the default value of the `success` flag to `False`.
5. Loop through each contact_data object in contacts_data.
6. Create a new contact record in Salesforce using the extracted contact details.
7. Add the ID of the created contact record to the `created_records` list.
8. If the loop completes without any errors, set the `success` flag to `True`.
9. Return the created_records and success flag as an instance of PushToSalesforceOutputDict.

## External Dependencies

The component depends on the following external libraries:

- `fastapi`: A modern, fast web framework for building APIs with Python.
- `pydantic`: A data validation and parsing library for Python.
- `simple_salesforce`: A library that simplifies communication with Salesforce APIs.

## API Calls

The component makes the following API calls using the Simple Salesforce library:

1. `sf.Contact.create()`: A call to the Salesforce API to create a new contact record. The method takes a contact dictionary containing the contact's details as input and returns a dictionary containing the ID of the created record.

## Error Handling

The component handles errors by wrapping the contact creation loop in a try-except block. If any exceptions occur during the creation process, the component prints an error message, including the exception's details. The `success` flag remains `False` in this case.

## Examples

To use the PushToSalesforce component within a Yeager Workflow, follow these steps:

1. Create an instance of `PushToSalesforceInputDict` with your Salesforce credentials and a list of contact details to be pushed to Salesforce:

