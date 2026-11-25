import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.models import organization, user, product  # noqa: F401 - register SQLAlchemy models
from app.routes.auth_routes import router as auth_router
from app.routes.product_routes import router as product_router
from app.routes.dashboard_route import router as dashboard_router

app = FastAPI(title="StockFlow Inventory MVP")

allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {"message": "StockFlow API is running"}
