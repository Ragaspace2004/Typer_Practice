import typer
from rich.console import Console
from rich.progress import Progress
import time

app = typer.Typer()
console = Console()

@app.command()
def process(task_name: str, total_steps: int = typer.Option(10, "--total-steps", "-t")):
    """
    Simulate a long-running task with a progress bar.
    
    Args:
        task_name: Name of the task to display.
        total_steps: Total number of steps in the task.
    """
    console.print(f"[bold green]Starting {task_name}...[/bold green]")
    
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{task_name}[/cyan]", total=total_steps)
        
        for step in range(total_steps):
            time.sleep(0.2)  # Simulate work being done
            progress.update(task, advance=1)
    
    console.print(f"[bold green]{task_name} completed![/bold green]")

if __name__ == "__main__":
    app()
