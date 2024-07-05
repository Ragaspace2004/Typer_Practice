import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer()
console = Console()

def generate_response(message: str) -> str:
    return f"{message}"

@app.command()
def interactive():
    """
    Start an interactive chat session with the chatbot.
    """
    console.print("[bold yellow]Starting chat session. Type 'exit' to end the session.[/bold yellow]")
    while True:
        message = console.input("[bold blue]You:[/bold blue] ")
        if message.lower() == 'exit':
            console.print("[bold red]Ending chat session.[/bold red]")
            break
        response = generate_response(message)
        response_panel = Panel(f"[bold magenta]Bot:[/bold magenta] {response}", title="Command Details", border_style="magenta")
        console.print(response_panel)

if __name__ == "__main__":
    app()
