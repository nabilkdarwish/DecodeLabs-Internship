from src.data_loader import (
    load_role_skills_dataset,
    load_skills_catalog,
    convert_ids_to_skills
)

from src.recommender import get_recommendations
from src.skill_gap import analyze_skill_gap

from src.ui import (
    show_header,
    show_dashboard,
    show_best_match,
    show_skill_gap,
    show_skills_panel
)


def main():

    show_header()

    dataset = load_role_skills_dataset()

    skills_df = load_skills_catalog()

    # عرض المهارات من أول التشغيل
    show_skills_panel(
        skills_df
    )

    print(
        "\n📌 Enter skill numbers separated by commas"
    )

    print(
        "Examples: 1,2,3  |  1،2،3"
    )

    print(
        "\nSelected skills will be analyzed using TF-IDF and Cosine Similarity."
    )

    user_input = input(
        "\n🎯 Your Skills ➜ "
    ).strip()

    if not user_input:

        print(
            "\n❌ Please select at least one skill."
        )

        return

    try:

        user_input = (
            user_input
            .replace("،", ",")
            .replace(" ", "")
        )

        selected_ids = [
            int(x)
            for x in user_input.split(",")
            if x
        ]

    except ValueError:

        print(
            "\n❌ Invalid input."
        )

        return

    selected_skills = convert_ids_to_skills(
        selected_ids
    )

    if not selected_skills:

        print(
            "\n❌ No valid skills selected."
        )

        return

    user_skills = " ".join(
        selected_skills
    )

    recommendations = get_recommendations(
        dataset,
        user_skills
    )

    best_match = recommendations.iloc[0]

    matched, missing = analyze_skill_gap(
        ",".join(selected_skills),
        best_match["Skills"]
    )

    show_dashboard(
        recommendations,
        skills_df
    )

    show_best_match(
        best_match
    )

    show_skill_gap(
        matched,
        missing
    )


if __name__ == "__main__":
    main()