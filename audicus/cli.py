"""Console script for audicus."""

from __future__ import absolute_import, print_function, unicode_literals

import typer
from audicus import utils
from rich.console import Console


app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for audicus."""
    console.print("Replace this message by putting your code into "
               "audicus.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
