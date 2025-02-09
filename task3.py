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

def extract_topic_performance(topics_dict):
    """
    Extracts summarized performance data from topic-wise quiz history.
    
    :param topics_dict: Dictionary containing quiz performance data for each topic.
    :return: Dictionary with aggregated data per topic.
    """
    topic_summary = {}

    for topic, quizzes in topics_dict.items():
        total_attempted = sum(q["total_questions"] for q in quizzes)
        total_correct = sum(q["correct_answers"] for q in quizzes)
        total_incorrect = sum(q["incorrect_answers"] for q in quizzes)
        speed = sum(int(q["speed"]) for q in quizzes)

        topic_summary[topic] = {
            "total_attempted": total_attempted,
            "correct": total_correct,
            "incorrect": total_incorrect,
            "speed": speed
        }

    return topic_summary


def generate_performance_prompt(topics_dict):
    topic_data = extract_topic_performance(topics_dict)

    topic_details = "\n".join([
        f"- **{topic.capitalize()}**: Attempted: {data['total_attempted']}, Correct: {data['correct']}, "
        f"Incorrect: {data['incorrect']}, speed: {data['speed']}%" 
        for topic, data in topic_data.items()
    ])

    prompt = f"""
    You are an AI tutor analyzing a student's quiz performance. Below is the student's topic-wise performance data:

    {topic_details}

    **Task:**
        Identify topics where accuracy is **below 50%** (weak areas).
        Highlight topics showing **improvement trends** over time.
        Detect **fluctuating performance** (if accuracy varies by more than 30% across quizzes).
        Provide actionable recommendations:
       - **Key topics** to focus on
       - **Suggested question types** (conceptual, formula-based, application-based)
       - **Time management strategies**
       - **Study techniques & resources**
    
    Use a **motivational and structured** tone to guide the student. The insights should be **practical and easy to follow. Also leep it under 100 words**.
    """
    response = model.generate_content(prompt)
    return response.text


performance = generate_performance_prompt(topics)
print(performance)
