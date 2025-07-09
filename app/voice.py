# app/voice.py

import speech_recognition as sr
from app.memory import get_trip_summary, get_current_location
from app.google_maps import update_location

def transcribe_and_respond(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    query = text.lower()

    # Simulate movement for every request
    update_location()

    if "where am i" in query:
        return f"You are currently at: {get_current_location()}"
    elif "why did i leave" in query or "where was i going" in query:
        return get_trip_summary()
    else:
        return f"You said: {text}"