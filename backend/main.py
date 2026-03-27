from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"

client = InferenceClient(model=MODEL_ID, token=HF_TOKEN)


class Query(BaseModel):
    prompt: str


@app.post("/diagnose")
async def diagnose(query: Query):
    try:
        result = client.chat_completion(
            messages=[
                {"role": "system", "content": "You are an expert medical assistant helping doctors with diagnosis and treatment. Always respond in English only."},
                {"role": "user", "content": query.prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        return {"response": result.choices[0].message.content}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}


@app.get("/health")
async def health():
    return {"status": "ok"}
