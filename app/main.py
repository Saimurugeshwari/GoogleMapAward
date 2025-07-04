from fastapi import FastAPI
import gradio as gr
from fastapi.responses import RedirectResponse
import speech_recognition as sr

# Create FastAPI app
app = FastAPI()

# Example FastAPI route
@app.get("/ping")
def ping():
    return {"message": "FastAPI is working!"}

# Gradio transcribe function
def transcribe(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

# Gradio app
demo = gr.Interface(fn=transcribe, inputs=gr.Audio(type="filepath"), outputs="text")

# Mount Gradio inside FastAPI
from gradio import mount_gradio_app
app = mount_gradio_app(app, demo, path="/gradio")

# Optional redirect
@app.get("/")
async def root():
    return RedirectResponse(url="/gradio")
