def generate_prompt(resume, jd):

    return f"""
You are an expert interview coach.

Analyze the candidate's resume and job description.

Resume:
{resume}

Job Description:
{jd}

Generate:

1. 10 Technical Interview Questions specific to the role.
2. 5 Behavioral Questions.
3. 3 HR Questions.
4. Personalized Improvement Suggestions.
5. Personalized Learning Roadmap.
6. Recommended Skills to Learn.

Make the interview questions adaptive and role specific.
"""
