import pandas as pd
import numpy as np
import requests

quiz_data = requests.get("https://www.jsonkeeper.com/b/LLQT").json()
quiz_submission = requests.get("https://api.jsonserve.com/rJvd7g").json()
last_quizes = requests.get("https://api.jsonserve.com/XgAgFJ").json()
current_quiz_questions_df = pd.DataFrame(quiz_data['quiz']['questions'])
current_quiz_submission_df = pd.DataFrame([quiz_submission])
last_quizes_df = pd.DataFrame(last_quizes)
last_quizes_df = pd.concat([last_quizes_df, current_quiz_submission_df], ignore_index=True)

topic_stats = {}

for _, row in last_quizes_df.iterrows():
    topic = row["quiz"]["topic"].strip().lower()
    submitted_at = pd.to_datetime(row["submitted_at"])
    accuracy = float(row["accuracy"].rstrip(" %"))
    quiz_id = row["quiz"]["id"]

    if topic not in topic_stats:
        topic_stats[topic] = []

    topic_stats[topic].append({
        "quiz_id": quiz_id,
        "submitted_at": submitted_at,
        "accuracy": accuracy
    })

for topic in topic_stats:
    topic_stats[topic] = sorted(topic_stats[topic], key=lambda x: x["submitted_at"])

weak_areas = []
improving_topics = []
fluctuating_topics = []

for topic, quizzes in topic_stats.items():
    accuracies = [q["accuracy"] for q in quizzes]
    
    avg_accuracy = np.mean(accuracies)
    if avg_accuracy < 50:
        weak_areas.append((topic, avg_accuracy))

    if len(accuracies) > 1 and accuracies[-1] > accuracies[0]:
        improving_topics.append((topic, accuracies[0], accuracies[-1]))

    if len(accuracies) > 1 and max(accuracies) - min(accuracies) > 30:
        fluctuating_topics.append((topic, min(accuracies), max(accuracies)))

print("\n🔴 Weak Areas (Avg Accuracy < 50%):")
for topic, acc in weak_areas:
    print(f"  - {topic}: {acc:.2f}% avg accuracy")

print("\n🟢 Improving Topics (First vs Last Accuracy):")
for topic, start, end in improving_topics:
    print(f"  - {topic}: {start:.2f}% ➝ {end:.2f}%")

print("\n🟡 Fluctuating Topics (Large Accuracy Variations):")
for topic, min_acc, max_acc in fluctuating_topics:
    print(f"  - {topic}: {min_acc:.2f}% ↔ {max_acc:.2f}%")
