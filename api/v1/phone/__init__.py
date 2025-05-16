from fastapi import APIRouter

from .handlers import router


__all__ = ["phone"]


phone = APIRouter(tags=["Phone"])
phone.include_router(router=router)
