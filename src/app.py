"""Create Application."""
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def home():
    """Heartbeat response.

    :return: 'Welcome to Icecream' hearbeat string
    """
    _r = {"message": "Hello World. You are welcome!!"}
    return JSONResponse(content=_r)


@app.get("/health")
async def healthcheck():
    """System healthcheck

    :return: Health status!
    """
    _health = {"health": "OK"}
    return JSONResponse(content=_health)

@app.get("/error500")
async def raise500():
    """Raise a 500 error

    :return: 500 error message
    """
    a = 1
    b = 0
    try:
        c = a/b
        _health = {"health": "OK"}
    except ZeroDivisionError as zerr:    
        _health = {"health": "Total system failure", "error": zerr.__doc__}
    
    return JSONResponse(content=_health, status_code=500)

