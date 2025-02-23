📊 Learning Dashboard
This interactive Learning Dashboard, built with Streamlit, Pandas, and Plotly, provides insights into learning program performance, participant engagement, and feedback.

🚀 Features
Dynamic Filters: Filter by program, department, and training date.
KPI Metrics: Total participants, average completion, and feedback score.

Visualizations:
📈 Program Completion % by Department
🎓 Quiz Score Distribution
⏱️ Hours Spent per Participant
🥧 Completion Distribution by Program
Risk Detection: Highlights participants with less than 50% completion.
Export: Download filtered data as a CSV.
📦 Installation
Clone the Repository:
bash
Copy
Edit
git clone https://github.com/yourusername/learning-dashboard.git
cd learning-dashboard
Create Virtual Environment (Optional but Recommended):
bash
Copy
Edit
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\\Scripts\\activate
Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
🟢 Running the App
bash
Copy
Edit
streamlit run learning_dashboard.py
📊 Dataset
The app uses a sample dataset Learning_Dashboard_Fake_Dataset.csv with the following columns:

Name, Department, Program Name, Completion %, Quiz Score, Feedback Score, Hours Spent, Training Date
📤 Exporting Data
Filtered data can be downloaded using the Export Filtered Data button on the dashboard.

🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

📄 License
This project is licensed under the MIT License.
