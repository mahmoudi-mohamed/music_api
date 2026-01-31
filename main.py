from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
import tempfile
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy
import torch

app = FastAPI(title="Music API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load MusicGen model
musicgen_processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
musicgen_model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small", torch_dtype=torch.float16)
device = "cuda:0" if torch.cuda.is_available() else "cpu"
musicgen_model.to(device)


class TextRequest(BaseModel):
    text: str

@app.post("/musicgen")
def text_to_music(request: TextRequest):
    inputs = musicgen_processor(
        text=[request.text],
        padding=True,
        return_tensors="pt",
    ).to(device)

    audio_values = musicgen_model.generate(**inputs, max_new_tokens=256)
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as tmp_wav_file:
        wav_file_path = tmp_wav_file.name
        sampling_rate = musicgen_model.config.audio_encoder.sampling_rate
        scipy.io.wavfile.write(wav_file_path, rate=sampling_rate, data=audio_values[0, 0].cpu().numpy())
        
        with open(wav_file_path, "rb") as f:
            audio_bytes = f.read()

    audio_b64 = base64.b64encode(audio_bytes).decode("utf-8")
    return {"audio_base64": audio_b64}


@app.get("/")
def root():
    return {"message": "Music API is running!"}
