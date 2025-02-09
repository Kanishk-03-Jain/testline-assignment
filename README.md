# NEET Testline - Quiz Performance Analysis
## Project Overview
This project analyzes student quiz performance to provide personalized recommendations for improvement. By leveraging historical and current quiz data, it identifies strengths, weaknesses, and learning trends. The system generates actionable insights, helping students focus on key areas to enhance their preparation.

# Features
- Topic-wise Performance Analysis 📊
- Difficulty-level Trends 📈
- Accuracy vs. Quiz ID Chronological Visualization ⏳
- Student Persona Identification 🎭
- Actionable Improvement Suggestions 🏆
# Setup Instructions
### Prerequisites
Ensure you have Python installed (preferably Python 3.8+).

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/neet-testline-analysis.git
   cd neet-testline-analysis
    ```
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Start Jupyter Notebook:
    ```sh
    Open testline.ipynb in Jupyter and run all cells.
    ```

# Approach Description
1. Data Processing
- Extracts quiz data via API and converts it into three pandas DataFrames:
    - Current Quiz Submission
    - Current Quiz Details
    - Last 5 Quiz Submissions
- Standardizes topic names (case-insensitive, removes extra spaces).
- Maps topic-wise performance by aggregating total, correct, and incorrect answers.
- Stores difficulty-wise statistics.
2. Data Analysis & Trends
- Topic-Wise Analysis: Generates bar plots for total, correct, and incorrect answers.
    ![body_fluids_circulations](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/body_fluids_circulations.png)
    ![microbes_in_human_welfare](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/microbes_in_human_welfare.png)
    ![reproductive_health](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/reproductive_health.png)
- Difficulty-Level Performance: Visualizes trends for different difficulty levels.
    ![difficulty_level_trend](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/difficulty_level.png)
- Accuracy vs. Quiz ID: Chronologically plots student accuracy across quizzes.
    ![accuracy_vs_quiz_id](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/accuracy_curve.png)
- Performance Sorting: Ensures quiz history is sorted by timestamp.
3. Personalized Insights & Recommendations
- Identifies weak areas based on incorrect answers.
- Detects improvement trends (consistency, accuracy changes).
- Defines student persona (e.g., "Concept Master", "Inconsistent Learner", "Speedster").
- Generates AI-powered suggestions for topic focus, question types, and study strategies.
# Future Enhancements
- Adaptive Learning Paths – Suggest personalized study plans.
- Question-Type Analysis – Evaluate MCQs vs. theoretical questions.
- Time-Efficiency Insights – Identify speed improvements.
- Gamification – Reward students for progress.

🚀 Contributors: Kanishk Jain
📧 Contact: kanishkjain03082005@gmail.com