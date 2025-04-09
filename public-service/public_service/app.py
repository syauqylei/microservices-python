from fastapi import FastAPI
from public_service.routes import router


def make_app():
    app = FastAPI(title="Public API")
    app.include_router(router=router)

    return app
