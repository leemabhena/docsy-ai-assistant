from django.shortcuts import render
import requests
import json
import time
from audio.utils import transcribe, handle_uploaded_file
from audio.conversation_transcription import recognize_from_file
# from azure.storage.blob import BlobServiceClient
from rest_framework.decorators import api_view
from django.http import JsonResponse
from azure.storage.blob import BlobServiceClient

SUBSCRIPTION_KEY = "YourSubscriptionKey"
SERVICE_REGION = "YourServiceRegion"
storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=purduedataforgood;AccountKey=In5P04csbd0Tq22hBzk+LSYqu3pX2qvZt0HR1fvQwaohvZzXcm2M1hZ7NlEMX9plLU2K6LeXoMTu+ASt7Su0dg==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = 'audiofiles'
content_container_url = "https://purduedataforgood.blob.core.windows.net/audiofiles?sp=rl&st=2023-11-29T14:50:49Z&se=2023-11-29T22:50:49Z&spr=https&sv=2022-11-02&sr=c&sig=su3kygs4SaIp9LDmikb%2BMTYyV34t%2FemYVq4v%2BuBQLVo%3D"
# account_name = "purduedataforgood"
# account_key = "In5P04csbd0Tq22hBzk+LSYqu3pX2qvZt0HR1fvQwaohvZzXcm2M1hZ7NlEMX9plLU2K6LeXoMTu+ASt7Su0dg=="
url = "https://eastus.api.cognitive.microsoft.com/"
headers = {
    "Ocp-Apim-Subscription-Key": "783e5e15a95145f4b40098aaf6937e06",
    "Content-Type": "application/json"
}
properties = {
    "wordLevelTimestampsEnabled": False,
    "displayFormWordLevelTimestampsEnabled": False,
    "diarizationEnabled": True,
    "punctuationMode": "DictatedAndAutomatic",
    "profanityFilterMode": "Masked"
}
# data = {
#     "displayName": "My Transcription",
#     "description": "Speech Studio Batch speech to text",
#     "locale": "en-us",
#     "contentUrls": [
#         blob_uri
#     ],
#     "model": {
#         "self": "https://eastus.api.cognitive.microsoft.com/speechtotext/v3.2-preview.1/models/base/e830341e-8f47-4e0a-b64c-3f66167b751c"
#     },
#     "properties": properties,
#     "customProperties": {}
# }


@api_view(["POST"])
def audio_upload(request):

    if request.method == "POST":
        print("GOT HERE")
        audio_file = request.FILES["audio"]
        file_path = handle_uploaded_file(audio_file)
        recognize_from_file(file_path)
        # blob_name = audio_file.name
        # print("audiofile", audio_file.name)
        # # Create a BlobServiceClient
        # blob_service_client = BlobServiceClient.from_connection_string(
        #     storage_connection_string)
        # container_client = blob_service_client.get_container_client(
        #     CONTAINER_NAME)

        # # Create a new container if one doesn't exist
        # if not container_client.exists():
        #     blob_service_client.create_container(CONTAINER_NAME)

        # blob_client = blob_service_client.get_blob_client(
        #     container=CONTAINER_NAME, blob=blob_name)
        # blob_client.upload_blob(audio_file)
        # time.sleep(5)
        # # Speech service
        # blob_uri = blob_client.url
        # print("GOT HERE")
        # transcription_id = transcribe(blob_uri)
        # transcription_status = requests.get(
        #     f"https://eastus.api.cognitive.microsoft.com/speechtotext/v3.1/transcriptions/{transcription_id}", headers=headers)
        # print(transcription_status.text)
        # transcription_results = requests.get(
        #     f"https://eastus.api.cognitive.microsoft.com/speechtotext/v3.1/transcriptions/{transcription_id}/files", headers=headers)
        # name = transcription_results.json()["values"][0]["name"]
        # transcription_client = container_client.get_blob_client(blob=name)
        # data = transcription_client.download_blob().readall()
        # print(data)

    return JsonResponse({"data": "1"}, safe=False)
