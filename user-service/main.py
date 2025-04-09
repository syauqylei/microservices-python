import uvicorn
from user_service import create_logger
from user_service.app import make_app
from user_service.database import create_db_and_tables


app = make_app()

Logger = create_logger("user_service", "app")


@app.on_event("startup")
def on_startup():
    Logger.info("Initiating Database user_service")
    create_db_and_tables()
    Logger.info("Finished initiating database")


@app.get("/ping")
def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    port = 8001
    debug = True
    Logger.info("Starting listing service. PORT: {}, DEBUG: {}".format(port, debug))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=debug)
