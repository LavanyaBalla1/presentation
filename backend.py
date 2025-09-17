# backend/app.py
from fastapi import FastAPI, File, UploadFile
import replicate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.post("/ghibli")
async def ghibli_style(image: UploadFile = File(...)):
    image_bytes = await image.read()

    output = replicate.run(
        "stability-ai/stable-diffusion:db21e45",
        input={
            "image": image_bytes,
            "prompt": "A Studio Ghibli-style portrait of this person, soft colors, detailed anime background",
            "num_inference_steps": 30,
        }
    )

    return {"image_url": output[0]}  # Replace with actual output path
