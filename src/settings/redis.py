from pydantic import RedisDsn

from src.settings._base import BaseSettingsWithConfig


__all__ = ["RedisSettings"]


class RedisSettings(BaseSettingsWithConfig, env_prefix="REDIS_"):
    DSN: RedisDsn
