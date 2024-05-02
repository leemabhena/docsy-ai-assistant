import React, { useState } from "react";
import { ReactMic } from "react-mic";

const AudioRecorder = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);

  const onStart = () => {
    setIsRecording(true);
  };
  // Generate random name for audiofile
  const generateName = () => {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790';
    const charsLength = characters.length;
    for (let i = 0; i < 15; i++) {
      result += characters.charAt(Math.floor(Math.random() * charsLength));
    }
    console.log("something")
    console.log(result)
    return result
  }

  const onStop = async (recordedBlob) => {
    setAudioBlob(recordedBlob);
    setIsRecording(false);
    // Convert the Blob to a File
    console.log(generateName())
    const audioFile = new File([recordedBlob.blob], `audio5.wav`, {
      type: "audio/wav",
    });
    
    // Create a FormData object to send the audio file
    const formData = new FormData();
    formData.append("audio", audioFile);

    try {
      const response = await fetch("http://localhost:8000/", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Transcription result:", data.result);
        // Do something with the transcribed text, such as displaying it in your React app.
      } else {
        console.error("Failed to process audio:", response.statusText);
      }
    } catch (error) {
      console.error("Error during audio processing:", error);
    }
  };

  const onPlay = () => {
    setIsPlaying(true);
    const audioElement = new Audio(URL.createObjectURL(audioBlob.blob));
    audioElement.addEventListener("ended", () => setIsPlaying(false));
    audioElement.play();
  };

  const onStopPlay = () => {
    setIsPlaying(false);
  };

  const onStopRecording = () => {
    setIsRecording(false);
    
  };

  return (
    <div>
      <ReactMic
        record={isRecording}
        className="sound-wave"
        onStop={()=>{onStop}}
        onData={() => {}}
        strokeColor="#000000"
        backgroundColor="#FF4081"
      />
      <button onClick={onStart} disabled={isRecording || isPlaying}>
        Start Recording
      </button>
      <button onClick={onStopRecording} disabled={!isRecording || isPlaying}>
        Stop Recording
      </button>
      <button
        onClick={() => setAudioBlob(null)}
        disabled={!audioBlob || isRecording || isPlaying}
      >
        Clear Recording
      </button>
      <button
        onClick={onPlay}
        disabled={!audioBlob || isRecording || isPlaying}
      >
        Play Recording
      </button>
      {isPlaying && (
        <button onClick={onStopPlay} disabled={!isPlaying}>
          Stop Playing
        </button>
      )}
      {audioBlob && (
        <audio controls>
          <source src={URL.createObjectURL(audioBlob.blob)} type="audio/wav" />
        </audio>
      )}
    </div>
  );
};

export default AudioRecorder;
