from fastapi import FastAPI
from app.routes import utils_router, url_shortener
from app.core.database import Base, engine


app = FastAPI(title="DevBox API")

Base.metadata.create_all(bind=engine)

app.include_router(utils_router.router)
app.include_router(url_shortener.router)

@app.get('/')
def devbox():
    return {"detail": "devbox api"}