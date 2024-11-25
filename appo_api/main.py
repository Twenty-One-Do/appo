from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from appo_api.config import settings
from appo_api.core import module


def create_app() -> FastAPI:
    app = FastAPI(
        title="APPO API",
        description="APPO API",
    )

    module.add_routers(app, settings.INCLUDE_APPS)
    
    # add middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_origin_regex=settings.CORS_ORIGINS_REGEX,
        allow_credentials=True,
        allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
        allow_headers=settings.CORS_HEADERS,
    )

    return app
