from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .endpoints import router


def get_app() -> FastAPI:
    description = "Сервис оплат пустышек для проекта FundMatch"

    tags_metadata = [
    ]

    application = FastAPI(
        title="Mock payment service",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
        openapi_tags=tags_metadata,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_app()
app.include_router(router)
