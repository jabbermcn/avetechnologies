from typing import Annotated

from fastapi import Depends

from src.config import async_redis_client
from src.services.phone.phone import PhoneService


__all__ = ["PhoneServiceDepends"]


async def _get_phone_service() -> PhoneService:
    return PhoneService(storage=async_redis_client)


PhoneServiceDepends = Annotated[PhoneService, Depends(dependency=_get_phone_service)]
