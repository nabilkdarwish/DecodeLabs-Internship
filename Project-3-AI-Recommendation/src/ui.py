from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich.layout import Layout

console = Console()


def show_header():

    console.print(
        Panel.fit(
            "[bold cyan]🚀 AI CAREER RECOMMENDATION ENGINE PRO[/bold cyan]",
            border_style="bright_green"
        )
    )


def show_skills_panel(skills_df):

    skills_text = ""

    for _, row in skills_df.iterrows():

        skills_text += (
            f"[bold cyan]{row['ID']:>2}[/bold cyan] ➜ "
            f"{row['Skill']}\n"
        )

    console.print(
        Panel(
            skills_text,
            title="📘 AVAILABLE SKILLS",
            border_style="bright_blue"
        ),
        justify="right"
    )


def create_progress_bar(score):

    total = 20

    filled = int(
        (score / 100) * total
    )

    return (
        "█" * filled +
        "░" * (total - filled)
    )


def show_dashboard(
    recommendations,
    skills_df
):

    layout = Layout()

    layout.split_row(
    Layout(name="left", ratio=2),
    Layout(name="right", ratio=2)
)

    # =========================
    # Recommendations Table
    # =========================

    table = Table(
        title="🏆 TOP CAREER RECOMMENDATIONS",
        border_style="cyan",
        show_lines=True
    )

    table.add_column(
        "Rank",
        justify="center",
        style="bold yellow"
    )

    table.add_column(
        "Career",
        style="bold cyan"
    )

    table.add_column(
        "Score",
        justify="center",
        style="bold green"
    )

    table.add_column(
        "Progress",
        style="magenta"
    )

    medals = [
        "🥇",
        "🥈",
        "🥉",
        "4️⃣",
        "5️⃣"
    ]

    for i, (_, row) in enumerate(
        recommendations.iterrows()
    ):

        score = float(
            row["Match Score"]
        )

        table.add_row(
            medals[i],
            row["Role"],
            f"{score:.2f}%",
            create_progress_bar(score)
        )

    # =========================
    # Skills Panel
    # =========================

    skills_text = ""

    for _, row in skills_df.iterrows():

        skills_text += (
            f"[bold cyan]{row['ID']:>2}[/bold cyan] ➜ "
            f"{row['Skill']}\n"
        )

    layout["left"].update(

        Panel(
            table,
            title="📊 RESULTS",
            border_style="green"
        )

    )

    layout["right"].update(

        Panel(
            skills_text,
            title="📘 SKILLS",
            border_style="bright_blue"
        )

    )

    console.print(
        layout
    )


def show_best_match(best_match):

    score = float(
        best_match["Match Score"]
    )

    console.print(
        Panel(
            f"""
🏆 Career: {best_match['Role']}

📊 Match Score: {score:.2f}%

{create_progress_bar(score)}
""",
            title="🎯 BEST MATCH",
            border_style="green"
        )
    )


def show_skill_gap(
    matched,
    missing
):

    matched_text = "\n".join(
        f"✔ {skill.title()}"
        for skill in matched
    )

    missing_text = "\n".join(
        f"✖ {skill.title()}"
        for skill in missing
    )

    console.print(
        Columns(
            [
                Panel(
                    matched_text,
                    title="✅ MATCHED SKILLS",
                    border_style="green"
                ),

                Panel(
                    missing_text,
                    title="❌ MISSING SKILLS",
                    border_style="red"
                )

            ],
            expand=True
        )
    )