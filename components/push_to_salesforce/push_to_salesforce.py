
import os
from typing import Dict, List, Optional

import yaml
from fastapi import FastAPI
from pydantic import BaseModel
from simple_salesforce import Salesforce

from core.abstract_component import AbstractComponent


class PushToSalesforceInputDict(BaseModel):
    contacts_data: List[Dict]
    SalesforceCredentials: Dict


class PushToSalesforceOutputDict(BaseModel):
    created_records: List[int]
    success: bool


class PushToSalesforce(AbstractComponent):
    def transform(
        self, args: PushToSalesforceInputDict
    ) -> PushToSalesforceOutputDict:
        salesforce_credentials = args.SalesforceCredentials
        contacts_data = args.contacts_data

        sf = Salesforce(
            username=salesforce_credentials["username"],
            password=salesforce_credentials["password"],
            security_token=salesforce_credentials["security_token"],
        )

        created_records = []
        success = False

        try:
            for contact_data in contacts_data:
                contact = {
                    "FirstName": contact_data["first_name"],
                    "LastName": contact_data["last_name"],
                    "Email": contact_data["email"],
                    "Phone": contact_data["phone"],
                }
                result = sf.Contact.create(contact)
                created_records.append(result["id"])
            success = True
        except Exception as e:
            print(f"Error pushing contacts to Salesforce: {str(e)}")

        return PushToSalesforceOutputDict(created_records=created_records, success=success)


push_to_salesforce_app = FastAPI()


@push_to_salesforce_app.post("/transform/")
async def transform(
    args: PushToSalesforceInputDict,
) -> PushToSalesforceOutputDict:
    push_to_salesforce = PushToSalesforce()
    return push_to_salesforce.transform(args)

