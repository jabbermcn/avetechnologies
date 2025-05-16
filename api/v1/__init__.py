from fastapi import APIRouter

from api.v1.phone import phone


__all__ = ["v1"]

v1 = APIRouter(prefix="/v1")
v1.include_router(router=phone)
