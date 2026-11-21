
#Q4: Data Analyst Job Shortlisting

required = {"python", "sql", "excel", "statistics"}

applicants = [
    {"name": "Ram", "age": 24, "cgpa": 3.4, "skills": {"python", "excel", "html"}},
    {"name": "Sita", "age": 37, "cgpa": 3.8, "skills": {"python", "sql", "excel", "statistics"}},
    {"name": "Gita", "age": 26, "cgpa": 3.6, "skills": {"python", "sql", "statistics", "tableau"}},
    {"name": "Hari", "age": 29, "cgpa": 2.7, "skills": {"sql", "excel", "statistics", "python"}}
]

# Shortlisted applicants ko record
shortlisted = []

# Applicants ma bhayeka extra skills store garne
extra_skills = set()

# Each applicant ko information check garne
for person in applicants:

    name = person["name"]
    age = person["age"]
    cgpa = person["cgpa"]
    skills = person["skills"]

    if age < 21 or age > 35:
        print(f"{name}: rejected (age {age})")
        continue

    # Required ra applicant ko common skills nikalne
    matched = required.intersection(skills)

    # Required skills madhye applicant sanga nabhayeko skills
    missing = required.difference(skills)

    # Match percentage calculate garne
    percentage = (len(matched) / len(required)) * 100

    # Required list ma nabhayeka applicant ko skills
    extra = skills.difference(required)
    extra_skills.update(extra)

    if percentage >= 75 and cgpa >= 2.5:
        print(f"{name}: {percentage:.0f}% match, shortlisted, missing {sorted(missing)}")

        # Sorting ko lagi match, CGPA ra name store garne
        shortlisted.append((-percentage, -cgpa, name))
    else:
        print(f"{name}: {percentage:.0f}% match, not shortlisted, missing {sorted(missing)}")

# Highest match ra CGPA pahila aaune gari sort garne
shortlisted.sort()

# Sorted names matra nikalne
interview_order = [person[2] for person in shortlisted]

print("Interview order:", interview_order)
print("Extra skills seen (not required):", sorted(extra_skills))
