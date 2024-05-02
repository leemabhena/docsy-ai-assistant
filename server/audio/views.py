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
storage_connection_string = "DefaultEndpointsProtocol=https;AccountName=purduedataforgood;AccountKey=[ACCOUNT-KEY];EndpointSuffix=core.windows.net"
CONTAINER_NAME = 'audiofiles'
content_container_url = "https://purduedataforgood.blob.core.windows.net/audiofiles?sp=rl&st=2023-11-29T14:50:49Z&se=2023-11-29T22:50:49Z&spr=https&sv=2022-11-02&sr=c&sig=[SIG]"


url = "https://eastus.api.cognitive.microsoft.com/"
headers = {
    "Ocp-Apim-Subscription-Key": "SUBSCRIPTION KEY",
    "Content-Type": "application/json"
}
properties = {
    "wordLevelTimestampsEnabled": False,
    "displayFormWordLevelTimestampsEnabled": False,
    "diarizationEnabled": True,
    "punctuationMode": "DictatedAndAutomatic",
    "profanityFilterMode": "Masked"
}


@api_view(["POST"])
def audio_upload(request):

    if request.method == "POST":
        print("GOT HERE")
        audio_file = request.FILES["audio"]
        file_path = handle_uploaded_file(audio_file)
        recognize_from_file(file_path)

    return JsonResponse({"data": "1"}, safe=False)
