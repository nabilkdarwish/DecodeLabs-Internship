def analyze_skill_gap(user_skills, role_skills):

    user_set = {
        skill.strip().lower()
        for skill in user_skills.split(",")
    }

    role_set = {
        skill.strip().lower()
        for skill in role_skills.split()
    }

    matched = sorted(
        user_set.intersection(role_set)
    )

    missing = sorted(
        role_set.difference(user_set)
    )

    return matched, missing