# AI Resume Shortlisting System

A simple AI-based Resume Shortlisting System built using Python.  
This project helps in filtering and ranking resumes based on required job skills.

---

## Project Overview

This project reads candidate resumes from a file and compares their skills with the required job skills.

The system checks how many required skills are present in each resume and gives a score based on matching skills.

It is a beginner-friendly Artificial Intelligence project that demonstrates:

- Resume filtering
- Skill matching
- Basic AI logic
- File handling in Python

---

## Features

- Resume shortlisting system
- Skill-based candidate ranking
- Reads resume data from file
- Calculates candidate score
- Beginner-friendly Python project
- Simple AI logic implementation
- Console-based interface

---

## Technologies Used

- Python

---

## Concepts Used

This project helps in learning:

- Python Basics
- File Handling
- Lists
- Loops
- Conditional Statements
- String Operations
- AI-based Filtering Logic
- Resume Ranking System

---

## Project Structure

```text
AI-Resume-Shortlisting-System/
│
├── resume_shortlisting.py
├── resume.rtf
└── README.md
```

---

## How the System Works

1. The system reads resumes from `resume.rtf`
2. Required job skills are predefined
3. Each resume is checked for matching skills
4. Matching skills increase the candidate score
5. Final score is displayed for each candidate

---

## Required Job Skills

```python
job_skills = ["python", "machine learning", "sql", "ai"]
```

---

## resume.rtf Example

Create a file named `resume.rtf`

```text
Rahul: Python, SQL, AI
Priya: Java, HTML, CSS
Aman: Python, Machine Learning, AI, SQL
Sneha: C++, Data Structures
```

---

## Requirements

Make sure Python is installed on your system.

### Check Python Version

```bash
python --version
```

or

```bash
python3 --version
```

---

## How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/AI-Resume-Shortlisting-System.git
```

---

### Step 2: Open Project Folder

```bash
cd AI-Resume-Shortlisting-System
```

---

### Step 3: Run Python File

```bash
python resume_shortlisting.py
```

If `python` does not work, use:

```bash
python3 resume_shortlisting.py
```

---

## Example Output

```text
===== Resume Ranking System =====

Candidate: Rahul
Score: 3
----------------------

Candidate: Priya
Score: 0
----------------------

Candidate: Aman
Score: 4
----------------------

Candidate: Sneha
Score: 0
----------------------
```

---

## Error Handling

If the resume file is missing:

```text
resume.rtf file not found
```

---

## Future Improvements

- GUI using Tkinter
- Resume upload system
- NLP-based skill extraction
- PDF resume support
- Machine Learning ranking
- Database integration
- Web application using Flask

---

## Learning Outcomes

By building this project, you can learn:

- Resume filtering techniques
- AI-based scoring systems
- Python file handling
- String matching logic
- Basic recruitment automation
- Beginner AI concepts

---
