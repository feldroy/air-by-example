import marimo

__generated_with = "0.14.7"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # Air by Example Index

    This is a collection of Air-powered websites, from simple to complex. The goal is to teach you how to build your own Air sites by studying ours.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## 01 Hello, World""")
    return


@app.cell
def _(mo):
    mo.md(r"""## 02 Hello, HTMX""")
    return


if __name__ == "__main__":
    app.run()
