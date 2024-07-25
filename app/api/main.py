from fastapi import Depends, FastAPI, Request, Response
from .database import SessionLocal
from . import router_users, router_items, router_sec


app = FastAPI()
app.include_router(router_users.router, tags=["USERS"])
app.include_router(router_items.router, tags=["ITEMS"])
app.include_router(router_sec.router, tags=["SECURITY"])


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
