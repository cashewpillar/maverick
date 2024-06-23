from typing import Any
from fastapi.routing import APIRoute

def parse_cors(v: Any) -> list[str] | str:
  if isinstance(v, str) and not v.startswith("["):
      return [i.strip() for i in v.split(",")]
  elif isinstance(v, list | str):
      return v
  raise ValueError(v)

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"