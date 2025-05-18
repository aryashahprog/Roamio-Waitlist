from fastapi import FastAPI
from models import UserProfile, NudgeRule, NudgeDeliveryLog
from typing import List
from datetime import datetime
import math
import time

app = FastAPI()

# In-memory storage for user profiles, nudge rules, and delivery logs
user_profiles: List[UserProfile] = []
nudge_rules: List[NudgeRule] = []
delivery_log: List[NudgeDeliveryLog] = []

@app.get("/")
def read_root():
    return {"message": "Nudge backend is running!"}

@app.post("/update-location")
def update_location(profile: UserProfile):
    # Add or update user profile in memory
    for idx, user in enumerate(user_profiles):
        if user.userId == profile.userId:
            user_profiles[idx] = profile
            break
    else:
        user_profiles.append(profile)
    return {"status": "Location received", "userId": profile.userId, "location": profile.lastLocation}

@app.get("/users")
def get_users():
    return user_profiles

@app.post("/create-nudge")
def create_nudge(nudge: NudgeRule):
    nudge_rules.append(nudge)
    return {"status": "Nudge created", "nudgeId": nudge.nudgeId}

@app.get("/delivery-log")
def get_delivery_log():
    return delivery_log

# Helper: Haversine distance in meters
def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

# Helper: Check if current time is within active window
def is_within_time_window(activeTime):
    now = datetime.now().strftime("%H:%M")
    return activeTime["start"] <= now <= activeTime["end"]

# Helper: Check for recent delivery (deduplication)
def was_recently_delivered(userId, nudgeId, window_seconds=7200):
    now = int(time.time())
    for log in delivery_log:
        if log.userId == userId and log.nudgeId == nudgeId:
            if now - log.timestamp < window_seconds:
                return True
    return False

@app.post("/run-nudge-engine")
def run_nudge_engine():
    results = []
    now_ts = int(time.time())
    for user in user_profiles:
        if not user.lastLocation:
            continue
        for nudge in nudge_rules:
            # Check distance
            dist = haversine(
                user.lastLocation.lat, user.lastLocation.lng,
                nudge.location.lat, nudge.location.lng
            )
            if dist > nudge.radius_m:
                continue
            # Check time window
            if not is_within_time_window(nudge.activeTime):
                continue
            # Check interest tag match
            if not set(user.interests).intersection(set(nudge.interestTags)):
                continue
            # Check deduplication
            if was_recently_delivered(user.userId, nudge.nudgeId):
                continue
            # Log delivery
            delivery_log.append(NudgeDeliveryLog(userId=user.userId, nudgeId=nudge.nudgeId, timestamp=now_ts))
            results.append({
                "userId": user.userId,
                "nudgeId": nudge.nudgeId,
                "title": nudge.title,
                "message": nudge.message
            })
    return {"nudges_to_send": results} 