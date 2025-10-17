import typer
import requests
import os


def summary():

    response = requests.post("http://127.0.0.1:8000/summarize", json={"path":os.getcwd()})


    response_json = response.json()



    if "summary" in response_json:      
        typer.echo(f'{response.json()["summary"]}')
    else:
        typer.echo(f'{response.json()["error"]}')