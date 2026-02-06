from fastapi import APIRouter, UploadFile
import openai
import tempfile
import os

router = APIRouter()

@router.post("/audio/upload")
async def upload_audio(file: UploadFile):
    suffix = os.path.splitext(file.filename)[-1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(await file.read())
        temp_path = temp.name

    transcript = openai.Audio.transcribe(
        model="whisper-1",
        file=open(temp_path, "rb")
    )

    return {
        "text": transcript["text"],
        "audio_url": temp_path
    }
