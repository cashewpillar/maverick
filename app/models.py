from datetime import datetime
from pydantic import model_validator
from sqlmodel import Field, SQLModel

class PKModel(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True, index=True)

class NoteBase(SQLModel):
  title: str | None = None
  content: str | None = None
  status: str | None = None
  # tags: list[str] = Field(sa_column=Column(list, index=True, nullable=True))
  # tags: list[str] = Field(default=[], sa_column=Field(JSON))
  reminder: datetime | None = None
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now, nullable=True)

class NoteCreate(NoteBase):
  @model_validator(mode='before')
  def required_title_or_content(cls, values):
    title = values.get("title")
    content = values.get("content")
    if not title and not content:
      raise ValueError("Either title or content is required")
    return values

class NoteUpdate(NoteBase):
  updated_at: datetime = Field(default_factory=datetime.now)

class Note(NoteBase, PKModel):
  pass