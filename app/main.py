from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import io
import soundfile as sf

from app.tts import generar_audio

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/tts")
def tts(text: str):
    audio = generar_audio(text)

    buffer = io.BytesIO()
    sf.write(buffer, audio, 24000, format="WAV")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="audio/wav")
