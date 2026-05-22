from rich.console import Console
from rich.table import Table
from rich import box

console = Console()


def show_chart(results):

    table = Table(
        title="AI Accuracy Visualization",
        box=box.DOUBLE_EDGE,
        border_style="bright_magenta"
    )

    table.add_column(
        "Model",
        style="bold cyan",
        justify="left"
    )

    table.add_column(
        "Accuracy",
        style="bold white",
        justify="center"
    )

    table.add_column(
        "Performance",
        justify="left"
    )

    colors = [
        "green",
        "cyan",
        "yellow",
        "magenta"
    ]

    for i, item in enumerate(results):

        accuracy = item["accuracy"]

        bars = "█" * int(accuracy / 4)

        color = colors[i]

        table.add_row(

            item["model"],

            f"[bold {color}]{accuracy}%[/bold {color}]",

            f"[{color}]{bars}[/{color}]"

        )

    console.print(table)