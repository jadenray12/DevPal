# cli/main.py
import typer
from cli.commands import commit  
# 1️⃣ Create a Typer app instance
# This holds all the CLI commands (like 'devpal commit', 'devpal explain', etc.)
app = typer.Typer(help="DevPal — your local AI code assistant")

# 2️⃣ Add subcommands
app.add_typer(commit.app, name="commit")

# 3️⃣ This is the entry point Typer uses when you run `devpal`
def main():
    app()

# 4️⃣ This makes it runnable directly via `python -m devpal.cli.main`
if __name__ == "__main__":
    main()
