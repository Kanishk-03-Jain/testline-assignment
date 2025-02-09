# NEET Testline - Quiz Performance Analysis
## Project Overview
This project analyzes student quiz performance to provide personalized recommendations for improvement. By leveraging historical and current quiz data, it identifies strengths, weaknesses, and learning trends. The system generates actionable insights, helping students focus on key areas to enhance their preparation.

## Features
- Topic-wise Performance Analysis 📊
- Difficulty-level Trends 📈
- Accuracy vs. Quiz ID Chronological Visualization ⏳
- Student Persona Identification 🎭
- Actionable Improvement Suggestions 🏆
## Setup Instructions
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
    or 
    You can also run .py files for each task separately.
    task1 is visualization of data. It is only inlcuded in jupyter notebook.
    ```sh
    python task2.py
    python task3.py
    python bonus_task1.py
    python bonus_task2.py
    ```

## Approach Description
### **1. Data Processing**
- Extracts quiz performance data from API endpoints and converts them into structured Pandas DataFrames.
- Cleans and normalizes topic names (removing extra spaces and making case-insensitive comparisons).
- Aggregates statistics on:
  - **Total Questions Attempted**
  - **Correct Answers**
  - **Incorrect Answers**
  - **Unattempted Questions**
- Sorts data chronologically using the `submitted_at` timestamp.

 ### **2. Task 1 - Data Analysis & Trends**
- **Topic-Wise Analysis:** Generates bar plots for total, correct, and incorrect answers.
    ![body_fluids_circulations](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/image_assets/body_fluids_circulations.png)
    ![microbes_in_human_welfare](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/image_assets/microbes_in_human_welfare.png)
    ![reproductive_health](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/image_assets/reproductive_health.png)

- **Difficulty-Level Performance:** Visualizes trends for different difficulty levels.
    ![difficulty_level_trend](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/image_assets/difficulty_level.png)

- **Accuracy vs. Quiz ID:** Chronologically plots student accuracy across quizzes.
    ![accuracy_vs_quiz_id](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/image_assets/accuracy_curve.png)

### **3. Task 2 - Generate Insights:**
- **Weak Area Identification**:
  - Detects topics with consistently low accuracy.
  - Highlights topics where incorrect answers outweigh correct answers.
- **Improvement Trends**:
  - Tracks progress over multiple quizzes.
  - Identifies whether accuracy is improving, stagnating, or declining for each topic.
- **Performance Gaps**:
  - Analyzes difficulty levels where the student struggles.
  - Detects topics where speed is low, indicating potential conceptual difficulties.
```sh
    🔴 Weak Areas (Avg Accuracy < 50%):
    - human reproduction: 38.00% avg accuracy
    - principles of inheritance and variation: 30.00% avg accuracy

    🟢 Improving Topics (First vs Last Accuracy):
    - body fluids and circulation: 50.00% ➝ 90.00%
    - reproductive health: 43.00% ➝ 100.00%

    🟡 Fluctuating Topics (Large Accuracy Variations):
    - body fluids and circulation: 31.00% ↔ 100.00%
    - reproductive health: 43.00% ↔ 100.00%
  ```

### **4. Task 3 - Create Recommendations:**
This task generates personalized recommendations to improve weak areas, optimize study strategies, and suggest focus areas based on quiz performance.
- Extract topic-wise performance metrics from `last_quizes_df`, including accuracy, speed, and skipped questions.  
- Identify weak topics where accuracy is below 50% or performance is declining.  
- Detect trends by analyzing moving average accuracy and response time across quizzes.  
- Categorize topics as Comfortable, Struggled, or Unattempted based on accuracy and attempt history.  
- Generate actionable recommendations, such as revising weak topics, focusing on specific question types, or improving time management.  
- Use an LLM to create structured study plans tailored to the student’s strengths and weaknesses.  

```sh
    Okay, let's boost your performance! Your strong areas are "Microbes," "Human Health," and "Body Fluids."

    **Areas for Improvement (Accuracy < 50%):** "Human Reproduction," "Principles of Inheritance," "Respiration," and "Structural Organisation." Focus on conceptual understanding and application-based questions in these areas.

    **Recommendations:** Practice consistently, manage time effectively during quizzes, and explore visual aids like diagrams and flowcharts for better comprehension. Use online resources and textbooks. Don't be discouraged; consistent effort will lead to success!
  ```

### **5. Bonus Task 1 - Student Persona Identification:**
This step defines a student’s learning profile based on their quiz performance patterns.

- Analyze topic-wise accuracy, speed, and consistency across multiple quizzes.  
- Cluster students into personas such as **"Concept Master"** (high accuracy, slow speed), **"Fast Learner"** (moderate accuracy, high speed), **"Struggling Learner"** (low accuracy, inconsistent performance), etc.  
- Detect strong and weak areas by tracking improvement trends and stagnation.  
- Use probabilistic modeling to estimate the student’s expected NEET rank based on historical NEET results and quiz accuracy.  
- Generate insights to help students focus on key areas for maximum score improvement.  
```sh
    **Analysis:**

    The student shows strength in "Microbes in Human Welfare" and "Human Health and Disease." They struggle with "Principles of Inheritance and Variation," "Respiration and Gas Exchange," and "Structural Organisation in Animals." "Body Fluids and Circulation" shows promising improvement over time.

    **Persona:** Developing Learner - exhibits potential but needs focused effort.

    **Recommendations:** Prioritize foundational understanding in weaker areas. Implement spaced repetition for memorization-heavy topics. Review incorrect answers immediately. Focus on fewer questions with deep understanding over broad, shallow attempts.

    **Trend:** Shows improvement in "Body Fluids and Circulation" suggesting adaptive learning capabilities. Keep up the great work!
```

### **6. Bonus Task 2 - Probabilistic Model for predicting Ranks based on marks:**
This step predicts a student’s potential NEET rank using machine learning.

- Created a synthetic dataset of **marks vs. ranks** based on past NEET results.  
- Scaled the data for better model performance.  
- Trained an **XGBoost regression model** with **marks and exam year** as input features to predict ranks.  

```sh
    Mean Absolute Error (MAE): 6553.521792833945
    Root Mean Squared Error (RMSE): 80.95382506610757
```

![model_curve](https://github.com/Kanishk-03-Jain/testline-assignment/blob/main/image_assets/model_curve.png)

## Future Enhancements
- Adaptive Learning Paths – Suggest personalized study plans.
- DKT(Deep Knowledge Tracing) + BERT – Predict student performance. It requires a large dataset.
- Time-Efficiency Insights – Identify speed improvements.
- Gamification – Reward students for progress.

Contributors: Kanishk Jain
Contact: kanishkjain03082005@gmail.com