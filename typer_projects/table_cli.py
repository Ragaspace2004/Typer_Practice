import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def show_table():
    """
    Display a styled table.
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Age", justify="right")
    table.add_column("Location", style="bold yellow")

    table.add_row("Alice", "24", "New York")
    table.add_row("Bob", "30", "London")
    table.add_row("Charlie", "28", "San Francisco")

    console.print(table)

if __name__ == "__main__":
    app()
