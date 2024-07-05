import typer
import json
from rich.console import Console
from rich.table import Table

app = typer.Typer()

tasks_file = "tasks.json"

console = Console()

def load_tasks():
    try:
        with open(tasks_file, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

# Command: add
@app.command()
def add(task: str):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    console.print(f"Task '{task}' added to the list.", style="bold green")

# Command: list
@app.command()
def list():
    tasks = load_tasks()
    if not tasks:
        console.print("No tasks found.", style="bold yellow")
    else:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Task")
        table.add_column("Status")
        for task in tasks:
            status = "[green]✓[/green]" if task["done"] else "[red]✗[/red]"
            table.add_row(task["task"], status)
        console.print(table)

# Command: done
@app.command()
def done(index: int = typer.Argument(..., help="Index of the task to mark as done.")):
    tasks = load_tasks()
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
        console.print(f"Task '{tasks[index]['task']}' marked as done.", style="bold green")
    except IndexError:
        console.print(f"Invalid task index '{index}'.", style="bold red")

# Command: delete
@app.command()
def delete(index: int = typer.Argument(..., help="Index of the task to delete.")):
    tasks = load_tasks()
    try:
        deleted_task = tasks.pop(index)["task"]
        save_tasks(tasks)
        console.print(f"Task '{deleted_task}' deleted from the list.", style="bold green")
    except IndexError:
        console.print(f"Invalid task index '{index}'.", style="bold red")


if __name__ == "__main__":
    app()

