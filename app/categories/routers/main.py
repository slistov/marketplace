from fastapi import FastAPI

from app.categories.routers import categories

app = FastAPI()

app.include_router(prefix="", router=categories.router)
