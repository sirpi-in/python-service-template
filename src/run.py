import uvicorn

from .main import app


def local():
    uvicorn.run("src.main:app", port=5001, use_colors=True, reload=True)


def server():
    uvicorn.run(app, host="0.0.0.0", port=5001, use_colors=True)
