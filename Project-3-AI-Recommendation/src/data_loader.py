from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"


def load_role_skills_dataset():

    return pd.read_csv(
        DATA_DIR / "role_skills_mapping.csv"
    )


def load_skills_catalog():

    return pd.read_csv(
        DATA_DIR / "skills_catalog.csv"
    )


def get_skill_mapping():

    skills_df = load_skills_catalog()

    return dict(
        zip(
            skills_df["ID"],
            skills_df["Skill"]
        )
    )


def convert_ids_to_skills(
    selected_ids
):

    mapping = get_skill_mapping()

    skills = []

    for skill_id in selected_ids:

        if skill_id in mapping:

            skills.append(
                mapping[skill_id]
            )

    return skills