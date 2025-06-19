from fastapi import APIRouter, HTTPException
from app.schemas.json_schema import JSONInput, JSONOutput
import json

router = APIRouter(prefix="/utils", tags=["Utils"])

@router.post("/format-json", response_model=JSONOutput)
def format_json(data: JSONInput):
    try:
        parsed = json.loads(data.raw_json)
        formatted = json.dumps(parsed, indent=4)
        return { "formatted_json": formatted }
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    