from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware


__all__ = ["setup_middlewares"]


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(middleware_class=ProxyHeadersMiddleware, trusted_hosts=["*"])  # noqa
    app.add_middleware(middleware_class=GZipMiddleware)  # noqa
    app.add_middleware(middleware_class=TrustedHostMiddleware, allowed_hosts=("*",))  # noqa
    app.add_middleware(
        middleware_class=CORSMiddleware,  # noqa
        allow_origins=("*",),
        allow_methods=("*",),
        allow_headers=("*",),
        allow_credentials=True,
    )
