# English Text-to-Speech (TTS) API

This project provides a Text-to-Speech (TTS) API for English, using FastAPI for the backend and a React-based frontend. The TTS functionality is powered by the Piper TTS engine with the `en_US-amy-medium` voice model.

## Features

- **FastAPI Backend:** A robust and fast backend server.
- **React Frontend:** A simple and reactive user interface to interact with the API.
- **Piper TTS:** High-quality text-to-speech synthesis.
- **Easy to Run:** Simple setup for both backend and frontend.

## Technologies Used

- **Backend:**
  - FastAPI
  - Piper TTS
  - Uvicorn
- **Frontend:**
  - React
  - Vite
  - Axios

## Installation

### Backend

1.  Navigate to the root directory of the project.
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Frontend

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the required Node.js packages:
    ```bash
    npm install
    ```

## Usage

### Running the Backend

1.  From the root directory, run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```
2.  The API will be available at `http://127.0.0.1:8000`.

### Running the Frontend

1.  Navigate to the `frontend` directory.
2.  Start the Vite development server:
    ```bash
    npm run dev
    ```
3.  The frontend will be available at `http://localhost:5173` (or another port if 5173 is in use).

### API Endpoint

The API has a single endpoint for TTS conversion:

- **POST** `/tts`
  - **Request Body:**
    ```json
    {
      "text": "Hello, world!"
    }
    ```
  - **Response:**
    ```json
    {
      "audio_base64": "<base64_encoded_wav_audio>"
    }
    ```