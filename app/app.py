from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app import (
    include_routers,
    setup_middlewares,
)


__all__ = ["get_application"]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # noqa
    yield


def get_application() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        title="APP title",
        version="0.0.1",
        default_response_class=ORJSONResponse,
    )

    include_routers(app=app)
    setup_middlewares(app=app)

    return app
