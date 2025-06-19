from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from app.core.database import Base

class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(Text, nullable=False)
    short_url = Column(Text, nullable=False, unique=True)
    hit_count = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    request_count = Column(Integer, default=0)
    last_request_time = Column(TIMESTAMP, server_default=func.now())