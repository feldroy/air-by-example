import marimo

__generated_with = "0.14.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Explain: 01 Hello, World""")
    return


@app.cell
def _(mo):
    mo.md(r"""Hi, this is Audrey M. Roy Greenfeld, walking you through building Air websites by example. Here we start with the smallest possible example of a working Air site.""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Starter Imports""")
    return


@app.cell
def _(mo):
    mo.md(r"""The minimal imports you need to get started are:""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```python
    from fastapi import FastAPI
    from air import tags as __
    from air.responses import TagResponse
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    I like the `__` because it makes Air views more readable. As you compose more complex views, you'll appreciate it.

    If the `__` bothers you, use `t` or `tags`.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## What's an Air Website?""")
    return


@app.cell
def _(mo):
    mo.md(r"""An Air site is just a FastAPI site. That means you get everything FastAPI and Starlette give you, plus convenient hosting of your websites on Python hosts that support FastAPI.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```python
    app = FastAPI()
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Views""")
    return


@app.cell
def _(mo):
    mo.md(r"""The simplest Air site has just 1 view. Here, this view returns a simple HTML page with a H1 on it.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```python
    @app.get("/", response_class=TagResponse)
    def home():
        return __.H1("Hello, world")
    ```
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""The `H1` function here is a tag function. When executed, it returns the HTML you would expect. Try it out and view the source!""")
    return


if __name__ == "__main__":
    app.run()
