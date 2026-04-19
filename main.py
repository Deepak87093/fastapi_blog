from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
posts = {
    "id":101,
    "name": "Deepak kumar",
    "title": "Software developer",
    "address": "Jharkhand"
}

@app.get("/home", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})