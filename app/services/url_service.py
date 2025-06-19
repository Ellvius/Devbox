from sqlalchemy.orm import Session
from app.models.url_model import URL

def get_url_by_code(db: Session, code: str):
    return db.query(URL).filter(URL.short_url == code).first()

def insert_url(db: Session, short_url: str, long_url: str):
    db_url = URL(short_url=short_url, long_url=long_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def is_url_exists(db: Session, long_url: str):
    return db.query(URL).filter(URL.long_url == long_url).first() is not None