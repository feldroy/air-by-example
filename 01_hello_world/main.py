from fastapi import FastAPI
from air import tags
from air.responses import TagResponse


app = FastAPI()


@app.get("/", response_class=TagResponse)
def home():
    return tags.H1("Hello, world")
