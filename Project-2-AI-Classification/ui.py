from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.align import Align
from rich import box

console = Console()


def create_table(results):

    table = Table(

        title="[bold magenta]AI MODEL PERFORMANCE COMPARISON[/bold magenta]",

        box=box.DOUBLE_EDGE,

        border_style="bright_cyan",

        header_style="bold white"

    )

    table.add_column(

        "Model",

        style="bold cyan",

        justify="center",

        width=25

    )

    table.add_column(

        "Accuracy",

        justify="center",

        width=15

    )

    table.add_column(

        "Performance",

        justify="center",

        width=20

    )

    for item in results:

        accuracy = item["accuracy"]

        if accuracy >= 90:

            status = "[bold green]Excellent[/bold green]"
            acc_color = "green"

        elif accuracy >= 85:

            status = "[bold cyan]Very Good[/bold cyan]"
            acc_color = "cyan"

        elif accuracy >= 80:

            status = "[bold yellow]Good[/bold yellow]"
            acc_color = "yellow"

        else:

            status = "[bold red]Average[/bold red]"
            acc_color = "red"

        table.add_row(

            item["model"],

            f"[bold {acc_color}]{accuracy}%[/bold {acc_color}]",

            status

        )

    return table


def show_best_model(name, accuracy):

    panel = Panel(

        Align.center(

            f"[bold green]{name}[/bold green]\n\n"
            f"[bold white]Best Accuracy : {accuracy}%[/bold white]",

            vertical="middle"

        ),

        title="[bold cyan]BEST MODEL SELECTED[/bold cyan]",

        border_style="bright_green",

        padding=(1, 12)

    )

    console.print(panel)