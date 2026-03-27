# Medic AI

Clinical reasoning assistant powered by a fine-tuned LLM on HuggingFace.

# Project Structure

medic-ai/
─ backend/        # FastAPI server
─ frontend/       # React app

# Backend

cd backend
pip install -r requirements.txt

Start the server:

uvicorn main:app --reload

Backend runs at: http://localhost:8000

# Frontend

cd frontend
npm install
npm start

Frontend runs at: http://localhost:3000

# Usage

1. Start the backend first
2. Start the frontend
3. Open http://localhost:3000 in your browser
4. Describe patient symptoms, history, and vitals
5. Click Send
