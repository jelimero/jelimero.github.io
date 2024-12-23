import os
import frontmatter

MONTHS = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

def load_work_experience(directory):
    """Lädt und sortiert Work-Experience-Dateien."""
    work_experience = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r') as file:
                post = frontmatter.load(file)
                work_experience.append((post.metadata, post.content))
    print(work_experience)
    # Sortiere Work-Experience-Einträge nach Startdatum
    return sorted(
        work_experience,
        key=lambda exp: (exp[0]["year_started"], MONTHS[exp[0]["month_started"]]),
        reverse=True
    )

