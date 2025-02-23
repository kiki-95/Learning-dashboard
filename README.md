# 📊 Learning Dashboard
This interactive dashboard, built with Streamlit, Pandas, and Plotly, provides insights into learning program performance, engagement, and feedback.

## 🚀 Features
- **Dynamic filters:** Program, department, and date.
- **KPI metrics:** Participants, completion %, and feedback.
- **Visualizations:** Completion by department, quiz scores, hours spent.
- **Risk detection:** Highlights <50% completion.
- **Export:** Download filtered data as CSV.

## 🌐 View Dashboard
[Learning Dashboard](http://localhost:8503/)

## 📦 Installation
```bash
git clone https://github.com/yourusername/learning-dashboard.git
cd learning-dashboard
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
streamlit run learning_dashboard.py
