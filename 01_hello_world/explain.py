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
    mo.md(r"""The minimal imports you need to get started are:""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```python
    from fastapi import FastAPI
    from air import tags
    from air.responses import TagResponse
    ```
    """
    )
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
    mo.md(r"""The simplest Air site has just 1 view. Here, this view returns a simple HTML page with a H1 on it.""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ```python
    @app.get("/", response_class=TagResponse)
    def home():
        return tags.H1("Hello, world")
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
