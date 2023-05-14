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

@app.get("/add", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("add_car.html", {"request": request})

@app.get("/view_list", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("view_cars.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("search_cars.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})