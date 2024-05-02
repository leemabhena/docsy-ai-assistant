import time
import swagger_client
import logging
import requests
import os


def handle_uploaded_file(f):
    file_path = os.path.join('audio/', f.name)
    with open(file_path, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


def transcribe_from_single_blob(uri, properties):
    """
    Transcribe a single audio file located at `uri` using the settings specified in `properties`
    using the base model for the specified locale.
    """
    transcription_definition = swagger_client.Transcription(
        display_name="My transcription",
        description="Speech Studio Batch speech to text",
        locale="en-US",
        content_urls=[uri],
        properties=properties
    )

    return transcription_definition


def _paginate(api, paginated_object):
    """
    The autogenerated client does not support pagination. This function returns a generator over
    all items of the array that the paginated object `paginated_object` is part of.
    """
    yield from paginated_object.values
    typename = type(paginated_object).__name__
    auth_settings = ["api_key"]
    while paginated_object.next_link:
        link = paginated_object.next_link[len(
            api.api_client.configuration.host):]
        paginated_object, status, headers = api.api_client.call_api(link, "GET",
                                                                    response_type=typename, auth_settings=auth_settings)

        if status == 200:
            yield from paginated_object.values
        else:
            raise Exception(
                f"could not receive paginated data: status {status}")


def transcribe(blob_uri):
    logging.info("Starting transcription client...")

    # configure API key authorization: subscription_key
    configuration = swagger_client.Configuration()
    configuration.api_key["Ocp-Apim-Subscription-Key"] = "783e5e15a95145f4b40098aaf6937e06"
    configuration.host = f"https://eastus.api.cognitive.microsoft.com/speechtotext/v3.1"

    # create the client object and authenticate
    client = swagger_client.ApiClient(configuration)

    # create an instance of the transcription api class
    api = swagger_client.CustomSpeechTranscriptionsApi(api_client=client)

    # Specify transcription properties by passing a dict to the properties parameter. See
    # https://learn.microsoft.com/azure/cognitive-services/speech-service/batch-transcription-create?pivots=rest-api#request-configuration-options
    # for supported parameters.
    properties = swagger_client.TranscriptionProperties()
    properties.word_level_timestamps_enabled = True
    properties.display_form_word_level_timestamps_enabled = True
    properties.punctuation_mode = "DictatedAndAutomatic"
    # properties.profanity_filter_mode = "Masked"
    properties.destination_container_url = "https://purduedataforgood.blob.core.windows.net/audiofiles?sp=rcwl&st=2023-11-29T22:15:41Z&se=2023-11-30T06:15:41Z&sv=2022-11-02&sr=c&sig=b5mA9k659dhktsNOt9eftxizPBwbX%2F%2B6aYqLLkT8g70%3D"
    properties.time_to_live = "PT1H"

    # uncomment the following block to enable and configure speaker separation
    properties.diarization_enabled = True
    properties.diarization = swagger_client.DiarizationProperties(
        swagger_client.DiarizationSpeakersProperties(min_count=1, max_count=2))

    properties.language_identification = swagger_client.LanguageIdentificationProperties([
                                                                                         "en-US", "ja-JP"])

    # Use base models for transcription. Comment this block if you are using a custom model.
    transcription_definition = transcribe_from_single_blob(
        blob_uri, properties)

    # Uncomment this block to use custom models for transcription.
    # transcription_definition = transcribe_with_custom_model(client, RECORDINGS_BLOB_URI, properties)

    # uncomment the following block to enable and configure language identification prior to transcription
    # Uncomment this block to transcribe all files from a container.
    # transcription_definition = transcribe_from_container(RECORDINGS_CONTAINER_URI, properties)

    created_transcription, status, headers = api.transcriptions_create_with_http_info(
        transcription=transcription_definition)

    # get the transcription Id from the location URI
    transcription_id = headers["location"].split("/")[-1]

    # Log information about the created transcription. If you should ask for support, please
    # include this information.
    logging.info(
        f"Created new transcription with id '{transcription_id}' in region eastus")

    logging.info("Checking status.")

    completed = False

    while not completed:
        # wait for 5 seconds before refreshing the transcription status
        time.sleep(5)

        transcription = api.transcriptions_get(transcription_id)
        logging.info(f"Transcriptions status: {transcription.status}")

        if transcription.status in ("Failed", "Succeeded"):
            completed = True

        if transcription.status == "Succeeded":
            pag_files = api.transcriptions_list_files(transcription_id)
            for file_data in _paginate(api, pag_files):
                if file_data.kind != "Transcription":
                    continue

                audiofilename = file_data.name
                results_url = file_data.links.content_url
                results = requests.get(results_url)
                logging.info(
                    f"Results for {audiofilename}:\n{results.content.decode('utf-8')}")
        elif transcription.status == "Failed":
            logging.info(
                f"Transcription failed: {transcription.properties.error.message}")
        return transcription_id
