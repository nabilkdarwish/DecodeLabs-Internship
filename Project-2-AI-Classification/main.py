from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.align import Align
from rich.text import Text
from rich import box
import time

from model import train_models
from ui import create_table, show_best_model
from charts import show_chart

console = Console()

console.print()

title = Panel(

    Align.center(

        "[bold cyan]AI MODEL COMPARISON DASHBOARD[/bold cyan]\n"
        "[bold magenta]Project 2 - Data Classification Using AI[/bold magenta]\n\n"
        "[bold white]BY : NABIL K.DARWISH[/bold white]",

        vertical="middle"

    ),

    border_style="bright_blue",

    padding=(1, 8)

)

console.print(title)

console.print("\n[bold yellow]Loading Iris Dataset...[/bold yellow]")
time.sleep(1)

console.print("[bold green]Dataset Loaded Successfully[/bold green]\n")
time.sleep(1)

console.print("[bold yellow]Training AI Models...[/bold yellow]\n")

results, best_model, best_accuracy = train_models()

time.sleep(1)

table = create_table(results)

console.print(table)

show_best_model(best_model, best_accuracy)

show_chart(results)

console.print(

    Panel(

        Align.center(

            "[bold green]AI MODEL COMPARISON COMPLETED SUCCESSFULLY[/bold green]\n"
            "[bold cyan]System Ready[/bold cyan]",

            vertical="middle"

        ),

        border_style="bright_green",

        padding=(1, 5)

    )

)