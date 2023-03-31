
import pytest
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi.testclient import TestClient
from your_module import ScrapeNikeITPersonas, ScrapeNikeITPersonasInputDict, ScrapeNikeITPersonasOutputDict, scrape_nike_it_personas_app

client = TestClient(scrape_nike_it_personas_app)


def test_scrape_nike_it_personas_init():
    component = ScrapeNikeITPersonas()
    assert hasattr(component, "transform")


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (
            ScrapeNikeITPersonasInputDict(),
            ScrapeNikeITPersonasOutputDict(employees_data=[]),
        ),
        (
            ScrapeNikeITPersonasInputDict(),
            ScrapeNikeITPersonasOutputDict(
                employees_data=[
                    {"name": "Alice", "email": "alice@example.com"},
                    {"name": "Bob", "email": "bob@example.com"},
                ]
            ),
        ),
    ],
)
def test_scrape_nike_it_personas_transform(input_data, expected_output):
    component = ScrapeNikeITPersonas()
    output = component.transform(input_data)
    assert output == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        (
            ScrapeNikeITPersonasInputDict(),
            {"employees_data": []},
        ),
        (
            ScrapeNikeITPersonasInputDict(),
            {
                "employees_data": [
                    {"name": "Alice", "email": "alice@example.com"},
                    {"name": "Bob", "email": "bob@example.com"},
                ]
            },
        ),
    ],
)
def test_scrape_nike_it_personas_endpoint(input_data, expected_output):
    response = client.post("/transform/", json=input_data.dict())
    assert response.status_code == 200
    assert response.json() == expected_output
