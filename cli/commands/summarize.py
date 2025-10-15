import typer
import requests
import os


def summary():

    response = requests.post("http://127.0.0.1:8000/summarize", json={"path":os.getcwd()})

    typer.echo(f'{response.json()["summary"]}')