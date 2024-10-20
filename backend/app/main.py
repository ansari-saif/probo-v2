from fastapi import FastAPI
from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.event import router as event_router
from app.core.database import engine
from app.models.user import SQLModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(auth_router, prefix="/api/v1", tags=["authentication"])
app.include_router(event_router, prefix="/api/v1", tags=["events"])
