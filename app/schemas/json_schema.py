from pydantic import BaseModel

class JSONInput(BaseModel):
    raw_json: str
    

class JSONOutput(BaseModel):
    formatted_json: str