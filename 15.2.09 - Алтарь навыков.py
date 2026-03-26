

def analyze_skills(skills_dict):
    sorted_skills = sorted(skills_dict.items(), key=lambda x: (-x[1], x[0]))
    average_level = round(sum(skills_dict.values()) / len(skills_dict))
    above_average = sorted([key for key in skills_dict.keys() if skills_dict[key] > average_level])

    return {'sorted_skills': sorted_skills, 'above_average': above_average, 'average_level': average_level}


skills = {
    "Атака": 4,
    "Защита": 2,
    "Магия": 5,
    "Скорость": 5,
    "Удача": 3
}

print(analyze_skills(skills))