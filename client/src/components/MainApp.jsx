import React from "react";
import AudioRecorder from "./AudioRecorder";

const MainApp = () => {
  return (
    <div className="main__app">
      <p className="brand__name">
        Docsy <i className="fa-solid fa-stethoscope rotate"></i>
      </p>
      <div className="doctor__wrapper">
        <div className="doctor__profile">
          <img src="/src/assets/doctor.jpg" alt="Doctor" />
        </div>

        <h1 className="doctor__title">Dr. John Doe</h1>
        <span className="doctor__specialty">Specialist in Cardiology</span>

        <AudioRecorder />
      </div>
    </div>
  );
};

export default MainApp;
