# Docsy - Patient Form Automation

<iframe src="https://player.vimeo.com/video/942080263?h=469a00f809" width="640" height="564" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

Docsy is a revolutionary application designed to streamline the process of filling out patient forms. Leveraging the power of modern web technologies, Docsy records conversations between doctors and patients, processes the audio to extract valuable information, and fills out forms automatically, minimizing manual effort and enhancing accuracy.

## Features

- **Conversation Recording**: Securely record conversations directly from the web interface built with React.
- **Audio Processing**: Send recordings to a Django backend, which uses Azure AI Speech API for transcription and speaker diarization.
- **Intelligent Prompting**: Process the transcript through a Large Language Model (LLM) to extract Q&A pairs for patient questionnaires.
- **Data Review**: Doctors can review and edit the extracted information before finalizing the form.
- **Data Persistence**: Save the validated form data in the database securely.
- **PDF Generation**: Download the completed forms in PDF format for easy printing and archiving.

## Getting Started

To get started with Docsy, clone the repository and follow the setup instructions below.

### Prerequisites

- Node.js and npm
- Python with Django
- Azure API credentials

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/leemabhena/docsy.git
   ```
   
2. Navigate to the frontend directory and install dependencies:
   ```sh
   cd docsy/client
   npm install
   npm run dev
   ```

3. Navigate to the backend directory and set up the Django environment:
   ```sh
   cd docsy/backend
   python manage.py runserver
   ```

### Usage

To use Docsy:

1. Begin a new patient consultation and start recording.
2. Once the conversation is over, stop the recording. The audio will be processed and transcribed automatically.
3. Review and edit the information extracted from the conversation.
4. Confirm the accuracy of the patient form and save it to the database.
5. Download the completed form as a PDF.

