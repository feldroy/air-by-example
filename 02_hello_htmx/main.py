from fastapi import FastAPI
from air import tags
from air.responses import TagResponse


app = FastAPI()


@app.get("/", response_class=TagResponse)
def home():
    return tags.Html(
        tags.Script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.5/dist/htmx.min.js"),
        tags.H1("Hello, world"),
        tags.P("Click me", hx_get="/name"),
    )


@app.get("/name", response_class=TagResponse)
def name():
    return tags.P("My name is Air and I'm lots of fun")
