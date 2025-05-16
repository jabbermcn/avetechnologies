from app.middlewares.setup import setup_middlewares
from app.routers.setup import include_routers

from .app import get_application


__all__ = [
    "get_application",
    "include_routers",
    "setup_middlewares",
]
