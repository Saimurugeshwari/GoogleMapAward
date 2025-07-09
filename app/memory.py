# app/memory.py

from app import google_maps

trip_memory = {
    "destination": "",
    "purpose": "",
}

def start_trip(destination: str, purpose: str):
    trip_memory["destination"] = destination
    trip_memory["purpose"] = purpose
    return trip_memory

def get_trip_summary():
    return f"You left to go to {trip_memory['destination']} for {trip_memory['purpose']}."

def get_current_location():
    return google_maps.get_current_location()

