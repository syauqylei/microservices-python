import logging
import uvicorn

from public_service.app import make_app

app = make_app()


@app.get("/ping")
def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    port = 8002
    debug = True
    logging.info("Starting Public API service. PORT: {}, DEBUG: {}".format(port, debug))
    uvicorn.run(app, host="0.0.0.0", port=port)
