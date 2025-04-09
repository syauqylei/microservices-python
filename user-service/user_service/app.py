from fastapi import FastAPI
from user_service.routes import route as UserRoute


def make_app() -> FastAPI:
    app = FastAPI(
        title="User Service", description="This a sets of api that handles user logic"
    )
    app.include_router(UserRoute)
    return app
