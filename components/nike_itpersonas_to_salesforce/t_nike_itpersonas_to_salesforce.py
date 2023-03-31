
import pytest
from typing import Any, Dict, List
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow
from fastapi.testclient import TestClient

# Import the main FastAPI app from your source code
from yourapp import nike_it_personas_to_salesforce_app

client = TestClient(nike_it_personas_to_salesforce_app)


class MockSalesforceCredentials(BaseModel):
    organization_id: str
    password: str
    security_token: str
    username: str


class MockDataPushedToSalesforce(BaseModel):
    success: bool
    created_record_ids: List[str]


class MockNikeITPersonasToSalesforce(AbstractWorkflow):

    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: MockSalesforceCredentials, callbacks: Any
    ) -> MockDataPushedToSalesforce:
        return MockDataPushedToSalesforce(
            success=True,
            created_record_ids=["id1", "id2"]
        )


# Define test cases with mocked input and expected output data
test_data = [
    (
        {"organization_id": "org1", "password": "pwd1", "security_token": "token1", "username": "usr1"},
        {"success": True, "created_record_ids": ["id1", "id2"]}
    ),
    (
        {"organization_id": "org2", "password": "pwd2", "security_token": "token2", "username": "usr2"},
        {"success": True, "created_record_ids": ["id3", "id4"]}
    ),
    # Add more test cases here as needed
]


@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_nike_it_personas_to_salesforce_workflow(input_data: Dict[str, str], expected_output: Dict[str, Any]):
    # Instantiate the mocked component
    mocked_workflow = MockNikeITPersonasToSalesforce()

    # Convert input_data into a BaseModel instance
    input_args = MockSalesforceCredentials(**input_data)

    # Call the transform() method with the mocked input data
    response = client.post("/transform/", json=input_args.dict())

    # Check if the response has the expected data
    assert response.status_code == 200
    assert response.json() == expected_output
