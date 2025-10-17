# cli/commands/commit.py
import typer
import requests

app = typer.Typer(help="Commit-related commands")

@app.command()
def generate(message: str = typer.Argument(..., help="Commit message text")):
    """
    Example: devpal commit generate "add login system"
    """

    response = requests.post("http://127.0.0.1:8000/summarize")
    typer.echo(f"🧠 DevPal will implement this later: '{message}'")
