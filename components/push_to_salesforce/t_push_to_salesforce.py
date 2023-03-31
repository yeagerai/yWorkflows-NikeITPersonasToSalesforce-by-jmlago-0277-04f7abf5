
import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from pydantic import ValidationError

from PushToSalesforce import (
    PushToSalesforce,
    PushToSalesforceInputDict,
    PushToSalesforceOutputDict,
)

# Test cases with mocked input and expected output data
test_data = [
    (
        {
            "contacts_data": [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "johndoe@example.com",
                    "phone": "555-1234",
                },
            ],
            "SalesforceCredentials": {
                "username": "testuser",
                "password": "testpassword",
                "security_token": "testtoken",
            },
        },
        {"created_records": [1], "success": True},
    ),
    (
        {
            "contacts_data": [
                {
                    "first_name": "Jane",
                    "last_name": "Doe",
                    "email": "janedoe@example.com",
                    "phone": "555-5678",
                },
            ],
            "SalesforceCredentials": {
                "username": "testuser",
                "password": "testpassword",
                "security_token": "testtoken",
            },
        },
        {"created_records": [2], "success": True},
    ),
]


@pytest.mark.parametrize("input_dict, expected_output", test_data)
def test_push_to_salesforce(input_dict, expected_output):
    # Create a PushToSalesforce instance
    push_to_salesforce = PushToSalesforce()

    # Mock the Salesforce.create() method to return a simulated success response.
    # Update the response with an incremental record ID, based on contact_data.
    push_to_salesforce.sf = MagicMock()
    push_to_salesforce.sf.Contact.create = MagicMock(
        side_effect=lambda contact: {"id": input_dict["contacts_data"][0]["phone"].split('-')[1]}
    )

    # Test transform() method
    try:
        input_data = PushToSalesforceInputDict(**input_dict)
        result = push_to_salesforce.transform(input_data)
        assert result.dict() == expected_output
    except ValidationError as e:
        pytest.fail(f"Validation error: {str(e)}")


# Error handling and edge case scenarios
def test_push_to_salesforce_error_handling():
    push_to_salesforce = PushToSalesforce()

    # Mock the Salesforce.create() method to raise an exception
    push_to_salesforce.sf = MagicMock()
    push_to_salesforce.sf.Contact.create = MagicMock(
        side_effect=Exception("An error occurred")
    )

    input_data = PushToSalesforceInputDict(
        contacts_data=[],
        SalesforceCredentials={
            "username": "testuser",
            "password": "testpassword",
            "security_token": "testtoken",
        },
    )

    with pytest.raises(HTTPException):
        push_to_salesforce.transform(input_data)
