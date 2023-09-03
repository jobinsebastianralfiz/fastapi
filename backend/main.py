from apis.base import api_router  # new
from core.config import settings
from db.base import Base
from db.sessions import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"msg": "Hello FastAPI🚀"}
