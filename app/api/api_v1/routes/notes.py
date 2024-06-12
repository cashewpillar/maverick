from fastapi import APIRouter
from app.models import Note

router = APIRouter()

@router.post("/")
async def create_note(note: Note):
  return note

@router.get("/")
async def read_notes():
  return [{"message": "Hello World"}]

@router.get("/{note_id}")
async def read_note(note_id: int):
  return {"note_id": note_id}

@router.put("/{note_id}")
async def update_note(note_id: int, note: Note):
  return {"note_id": note_id, **note.model_dump()}