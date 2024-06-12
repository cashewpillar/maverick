from fastapi import APIRouter

from app.api.api_v1.routes import notes

api_router = APIRouter()
api_router.include_router(notes.router, prefix="/notes", tags=["items"])