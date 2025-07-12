import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import dotenv

dotenv.load_dotenv()

STORAGE_CONNECTION_STRING = os.getenv("YOUR_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "raw-data"
LOCAL_FILE_PATH = "../data/local_data.csv"
BLOB_NAME = "local_data.csv"

def upload_blob():
    try:
        blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

        with open(LOCAL_FILE_PATH, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"✅ Uploaded {LOCAL_FILE_PATH} to container '{CONTAINER_NAME}' as blob '{BLOB_NAME}'.")

    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    upload_blob()
