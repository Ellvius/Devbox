from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.schemas.url_schema import URLRequest, URLResponse
from app.core.dependencies import get_db
from app.services.url_service import insert_url, is_url_exists, get_url_by_code
from app.utils.code_generator import generate_uuid

router = APIRouter(prefix="/url", tags=["URL Shortener"])
    

@router.post("/shorten", response_model=URLResponse)
def shorten_url(req: Request, payload: URLRequest, db: Session = Depends(get_db)):
    code = generate_uuid()
    
    insert_url(db, code, str(payload.url))
    short_url = f"{req.base_url}url/s/{code}"
    return URLResponse(short_url=short_url)


@router.get("/s/{code}")
def redirect_to_url(code: str, db: Session = Depends(get_db)):
    result = get_url_by_code(db, code)
    if result:
        return RedirectResponse(url=str(result.long_url))
    else:
        raise HTTPException(status_code=404, detail="URL not found")