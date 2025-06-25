from fastapi import FastAPI
from air import tags as __
from air.responses import TagResponse


app = FastAPI()


@app.get("/", response_class=TagResponse)
def home():
    return __.H1("Hello, world")
