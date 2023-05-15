from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Dict
from models import *
import json
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/add", response_class=HTMLResponse)
async def add_car(request: Request):
    title_string="   Enter A New Car"
    return templates.TemplateResponse("add_car.html", {"request": request, "title_string":title_string})

@app.get("/view_list", response_class=HTMLResponse)
async def list_cars(request: Request):
    with open("cars.json") as f:
        cars = [json.loads(line) for line in f]
        cars=cars[0]

    sample=[
    {"Name": "Honda Civic", "Color": "Red", "Year": 2022, "State": "New"},
    {"Name": "Ford Mustang", "Color": "Black", "Year": 2018, "State": "Used"},
    {"Name": "Toyota Corolla", "Color": "Blue", "Year": 2020, "State": "New"},
    {"Name": "Nissan Altima", "Color": "White", "Year": 2019, "State": "Used"}]
    newcars=[]

    for car in cars:

        dic = json.loads(car)
        newcars.append(dic)




    return templates.TemplateResponse("view_cars.html", {"request": request, "cars": newcars,"sample":sample})

@app.get("/search", response_class=HTMLResponse)
async def search_cars(request: Request):
    return templates.TemplateResponse("search_cars.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_app(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/add")
async def add_car_post(request: Request, Name: str = Form(...), Color:str = Form(...), Year:int =Form(...), State:Cond = Form(...))->Dict:
    car ={}
    car["Name"]=Name
    car["Color"]=Color
    car["Year"]=Year
    car["State"]=State
    jcar= json.dumps(car)
    with open("cars.json", "r") as f:
        cars = json.load(f)
    if not isinstance(cars, list):
        cars = []
        print("no list found")

    # Append the new car JSON to the list
    cars.append(jcar)

    # Write the updated list of cars to the file
    with open("cars.json", "w") as f:
        json.dump(cars, f)
    title_string = f"   Success:  {Name} was added to the list"
    return templates.TemplateResponse("add_car.html", {"request": request, "title_string": title_string})
