from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Location(BaseModel):
    lat: float
    lng: float
    timestamp: Optional[int] = None

class UserProfile(BaseModel):
    userId: str
    interests: List[str]
    lastLocation: Optional[Location] = None
    notificationToken: Optional[str] = None

class NudgeRule(BaseModel):
    nudgeId: str
    title: str
    message: str
    location: Location
    radius_m: float
    interestTags: List[str]
    activeTime: Dict[str, str]  # {"start": "HH:mm", "end": "HH:mm"}

class NudgeDeliveryLog(BaseModel):
    userId: str
    nudgeId: str
    timestamp: int 