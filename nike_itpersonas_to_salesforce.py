
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class SalesforceCredentials(BaseModel):
    organization_id: str
    password: str
    security_token: str
    username: str


class DataPushedToSalesforce(BaseModel):
    success: bool
    created_record_ids: typing.List[str]


class NikeITPersonasToSalesforce(AbstractWorkflow):

    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: SalesforceCredentials, callbacks: typing.Any
    ) -> DataPushedToSalesforce:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        success = results_dict[0].success
        created_record_ids = results_dict[0].created_record_ids
        out = DataPushedToSalesforce(success=success, created_record_ids=created_record_ids)
        return out


load_dotenv()
nike_it_personas_to_salesforce_app = FastAPI()


@nike_it_personas_to_salesforce_app.post("/transform/")
async def transform(
    args: SalesforceCredentials,
) -> DataPushedToSalesforce:
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()
    return await nike_it_personas_to_salesforce.transform(args, callbacks=None)

