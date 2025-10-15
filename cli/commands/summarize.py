import typer
import requests


def summary():

    response = requests.post("http://127.0.0.1:8000/summarize")

    typer.echo(f'{response.json()["summary"]}')