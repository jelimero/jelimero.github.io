from ezcv import EzCV

def main():
    # Initialisiere ezcv
    site = EzCV()
    
    # Pfad zur Work-Experience
    work_experience_dir = os.path.join(site.content_dir, "work_experience")

    # Lade und sortiere die Work-Experience
    sorted_work_experience = load_work_experience(work_experience_dir)

    # Ersetze die unsortierten Daten durch sortierte
    site.data["work_experience"] = sorted_work_experience

    # Rendere die Seite
    site.render()

if __name__ == "__main__":
    main()