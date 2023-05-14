from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from models import *
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/test1", response_class=HTMLResponse)
async def test1(request: Request):
    return templates.TemplateResponse("test1.html", {"request": request})

@app.get("/test2", response_class=HTMLResponse)
async def test2(request: Request):
    return templates.TemplateResponse("test1.html", {"request": request})