# MapBuddy: Memory Support & Navigation Companion

MapBuddy is a voice-enabled navigation companion designed to help people with **short-term memory loss**, **amnesia**, or **early-stage dementia** travel independently and safely. Unlike traditional GPS apps, MapBuddy reminds users of their **trip purpose**, gives **current location awareness**, and helps them re-orient themselves when confused.
Joy doesn’t depend on memory—it lives in moments.

## Key Features

**Save the Input from the user:**  Before start the trip user enter 'where they are going and purpose" 
**Trip Purpose Reminder:** Reminds the user why they left home and where they are going.
**Live Location Awareness:** Answers “Where am I?” with street-level info and progress.
**Voice Interaction:** Supports voice queries like “What should I do now?”
**Caregiver Updates:** Optional live location sharing and notifications.
**Google Maps Guidance:** Turn-by-turn navigation support (customizable for walking trips).
**Safe Return:** Helps users navigate back home if they forget their goal.
**Emergency Mode:** Allows users or caregivers to trigger an SOS or alert.

## Tech Stack
### Backend:

* **FastAPI:** API layer and server logic
* **Gradio:** Voice interface for user interaction
* **SpeechRecognition:** Speech-to-text for audio commands
* **Google Maps API / OpenStreetMap:** Route planning, geolocation, and turn-by-turn navigation
* **Firebase / Supabase / MongoDB:** (Future) user trip/session storage, caregiver accounts

### Frontend (Future Phases):

* Gradio UI (prototype)
* Render for hosting
* React Native or Flutter mobile app (Future)

### Others:

* **Redis + Celery:** (Future) for background route calculations and queueing
* **WebSockets:** (Future) for real-time caregiver updates
* **Docker:** Containerization for easy deployment
* **GCP App Engine:** Hosting options

---
## Product Roadmap
-- product Roadmap.png

## Local Setup (Prototype)

```bash
# Clone the repo
-- git clone https://github.com/yourname/mapbuddy.git
--cd mapbuddy

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI with Gradio interface
uvicorn main:app --reload

# Access at: http://127.0.0.1:8000/gradio
```

## Future Users

* People with **short-term memory loss**, post-traumatic brain injury, early dementia
* Elderly individuals living alone
* Children walking to school alone
* Tourists in unfamiliar cities
* Field workers on complex walking routes

## Future Enhancements

* Real-time route deviation detection
* AI-based route correction
* Caregiver remote commands
* Wearable device integration (Apple Watch, Fitbit, etc.)
* Voice assistants (Google Assistant, Alexa, Siri)


