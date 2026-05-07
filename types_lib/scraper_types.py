from typing import List, Optional
from pydantic import BaseModel


class ScraperInputType(BaseModel):
    apps: List[str]


class ScraperResponse(BaseModel):
    app: str
    status: str  # "ok" | "error" | "unknown"

    genre: Optional[str] = None
    genre_id: Optional[str] = None

    category: Optional[str] = None
    distraction_value: Optional[int] = None

    error: Optional[str] = None
    reason: Optional[str] = None

# ---- request body model ----
class GenresRequest(BaseModel):
    apps: List[str]


# ---- response ----
class GenresResponse(BaseModel):
    results: List[ScraperResponse]
