import pandas as pd
import os
from dotenv import load_dotenv
import requests
import google.generativeai as genai

load_dotenv(dotenv_path=".env")
gemini_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=gemini_api_key)

quiz_data = requests.get("https://www.jsonkeeper.com/b/LLQT").json()
quiz_submission = requests.get("https://api.jsonserve.com/rJvd7g").json()
last_quizes = requests.get("https://api.jsonserve.com/XgAgFJ").json()
model = genai.GenerativeModel("gemini-2.0-flash")


current_quiz_questions_df = pd.DataFrame(quiz_data['quiz']['questions'])
current_quiz_submission_df = pd.DataFrame([quiz_submission])
last_quizes_df = pd.DataFrame(last_quizes)
last_quizes_df = pd.concat([last_quizes_df, current_quiz_submission_df], ignore_index=True)

topics = {}

for _, row in last_quizes_df.iterrows():
    quiz_id = row['quiz']['id']
    topic = row['quiz']['topic'].strip().lower()
    submitted_at = pd.to_datetime(row['submitted_at'])
    speed = row['speed']

    if topic not in topics:
        topics[topic] = []

    topics[topic].append({
        "quiz_id": quiz_id,
        "submitted_at": submitted_at,
        "total_questions": row["total_questions"],
        "correct_answers": row["correct_answers"],
        "incorrect_answers": row["incorrect_answers"],
        "speed": row['speed']
    })

for topic in topics:
    topics[topic] = sorted(topics[topic], key=lambda x: x["submitted_at"])

def generate_student_persona(topics):
    prompt = f"""
    Analyze the student's quiz performance and define their learning persona. Based on the given data, highlight their strengths, weaknesses, and improvement trends. Provide actionable recommendations for focused improvement.
    
    ### **Student's Performance Data**
    Each topic contains the number of total questions attempted, correct answers, incorrect answers, and submission timestamps.
    
    """
    
    for topic, quizzes in topics.items():
        prompt += f'    "{topic}": [\n'
        for quiz in quizzes:
            prompt += f'        {{"quiz_id": {quiz["quiz_id"]}, "submitted_at": "{quiz["submitted_at"]}", "total_questions": {quiz["total_questions"]}, "correct_answers": {quiz["correct_answers"]}, "incorrect_answers": {quiz["incorrect_answers"]}, "speed": "{quiz["speed"]}"}},\n'
        prompt += "    ],\n"
    
    prompt += """
    }
    
    ### **Task**  
    1. **Analyze Patterns** – Identify topics where the student is consistently strong or weak.  
    2. **Define Persona** – Assign a learning persona based on accuracy, consistency, speed, and trends (e.g., "Concept Master", "Speedster", "Inconsistent Learner", etc.).  
    3. **Highlight Weaknesses** – Identify subjects or question types where the student needs improvement.  
    4. **Provide Actionable Recommendations** – Suggest specific study techniques, time management strategies, or question types to focus on.  
    5. **Identify Performance Trends** – Determine if the student is improving, plateauing, or declining.  
    6. **Creative Insights** – Provide engaging feedback using an encouraging tone to help the student improve effectively.
    
    Ensure that the analysis is **very short under 100 words, structured, and actionable**.
    """
    response = model.generate_content(prompt)
    return response.text

persona = generate_student_persona(topics)
print(persona)