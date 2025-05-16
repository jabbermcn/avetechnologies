from redis.asyncio import Redis

from src.settings import settings


__all__ = ["async_redis_client"]

async_redis_client = Redis.from_url(url=settings.REDIS.DSN.unicode_string())
