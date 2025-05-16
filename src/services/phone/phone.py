from redis import RedisError
from redis.asyncio import Redis

from src.exceptions import (
    InternalServerError,
    ObjectAlreadyExistError,
    ObjectNotFoundError,
)
from src.types import PhoneDataDTO, PhoneDataCreateRequestDTO, PhoneDataUpdateRequestDTO

__all__ = ["PhoneService"]


class PhoneService:
    def __init__(self, storage: Redis) -> None:
        self.storage = storage

    async def get_data(self, phone: str) -> PhoneDataDTO:
        try:
            data = await self.storage.get(name=phone)
            if data is None:
                raise ObjectNotFoundError("phone_data")
            return PhoneDataDTO.model_validate_json(json_data=data)
        except RedisError:
            raise InternalServerError("redis")

    async def set_data(self, phone: str, data: PhoneDataCreateRequestDTO) -> PhoneDataDTO:
        try:
            existing = await self.storage.exists(phone)
            if existing:
                raise ObjectAlreadyExistError("phone_data")

            await self.storage.set(name=phone, value=data.model_dump_json())
            return await self.get_data(phone=phone)
        except RedisError:
            raise InternalServerError("redis")

    async def update_data(self, phone: str, data: PhoneDataUpdateRequestDTO) -> PhoneDataDTO:
        try:
            existing = await self.storage.exists(phone)
            if not existing:
                raise ObjectNotFoundError("phone_data")

            await self.storage.set(name=phone, value=data.model_dump_json())
            return await self.get_data(phone=phone)
        except RedisError:
            raise InternalServerError("redis")
