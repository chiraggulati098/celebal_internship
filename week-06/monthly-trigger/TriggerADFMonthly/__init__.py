import datetime
import logging
import os
import requests
import azure.functions as func
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")
RESOURCE_GROUP = os.getenv("RESOURCE_GROUP")
ADF_NAME = os.getenv("ADF_NAME")
PIPELINE_NAME = os.getenv("PIPELINE_NAME")

def is_last_saturday(date):
    next_week = date + datetime.timedelta(days=7)
    return date.weekday() == 5 and next_week.month != date.month

def main(mytimer: func.TimerRequest) -> None:
    utc_now = datetime.datetime.utcnow()
    today = utc_now.date()

    if is_last_saturday(today):
        logging.info("It's the last Saturday. Triggering ADF pipeline...")

        # Azure AD Token
        token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'resource': 'https://management.azure.com/'
        }
        token_response = requests.post(token_url, data=payload)
        access_token = token_response.json().get("access_token")

        adf_url = (
            f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/"
            f"resourceGroups/{RESOURCE_GROUP}/providers/Microsoft.DataFactory/"
            f"factories/{ADF_NAME}/pipelines/{PIPELINE_NAME}/createRun?api-version=2018-06-01"
        )

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        trigger_response = requests.post(adf_url, headers=headers)
        logging.info(f"ADF Trigger Response: {trigger_response.status_code} - {trigger_response.text}")
    else:
        logging.info("Today is not the last Saturday. Skipping.")
