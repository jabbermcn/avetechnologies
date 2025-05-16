from pathlib import Path
from typing import Annotated

from pydantic import Field

from src.settings._base import BaseSettingsWithConfig
from src.settings.redis import RedisSettings
from src.settings.server import ServerSettings


__all__ = ["settings"]


class Settings(BaseSettingsWithConfig):
    BASE_DIR: Path = Path(__file__).parent.parent

    SERVER: Annotated[ServerSettings, Field(default_factory=ServerSettings)]
    REDIS: Annotated[RedisSettings, Field(default_factory=RedisSettings)]


settings = Settings()
