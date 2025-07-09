from dotenv import load_dotenv
import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.memory import start_trip
from app.voice import transcribe_and_respond

# Load environment variables
load_dotenv()

app = FastAPI()

# Template folder is at the root level called "templates"
templates = Jinja2Templates(directory="templates")


@app.get("/ping")
def ping():
    return {"message": "FastAPI is working!"}


@app.post("/start_trip")
def start_trip_route(destination: str, purpose: str):
    data = start_trip(destination, purpose)
    return {"message": f"Trip started to {data['destination']} for {data['purpose']}"}


@app.get("/map", response_class=HTMLResponse)
async def map_view(request: Request):
    api_key = os.getenv("GMAPS_API_KEY")
    return templates.TemplateResponse("map.html", {"request": request, "google_maps_api_key": api_key})
