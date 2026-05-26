# AI Resume Shortlisting System

# Skills required for job

job_skills = ["python", "machine learning", "sql", "ai"]

try:

    # Open resume file

    file = open("resume.rtf", "r")

    # Read resumes

    resumes = file.readlines()

    # Close file

    file.close()

    print("===== Resume Ranking System =====")

    # Loop through resumes

    for resume in resumes:

        # Remove extra spaces/new line

        resume = resume.strip()

        # Skip empty lines

        if ":" not in resume:

            continue

        # Convert to lowercase

        data = resume.lower()

        # Split name and skills

        parts = data.split(":")

        name = parts[0]

        skills = parts[1]

        # Initial score

        score = 0

        # Match skills

        for skill in job_skills:

            if skill in skills:

                score += 1

        # Print result

        print("Candidate:", name.title())

        print("Score:", score)

        print("----------------------")

except FileNotFoundError:

    print("resume.rtf file not found")