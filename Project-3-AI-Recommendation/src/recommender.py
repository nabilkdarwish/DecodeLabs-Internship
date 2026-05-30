from src.similarity import calculate_similarity


def get_recommendations(df, user_skills):

    scores = calculate_similarity(
        user_skills,
        df["Skills"]
    )

    result_df = df.copy()

    result_df["Match Score"] = scores * 100

    recommendations = result_df.sort_values(
        by="Match Score",
        ascending=False
    )

    return recommendations.head(5)