import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("Learning_Dashboard_Fake_Dataset.csv")

df = load_data()

# Dashboard Title
st.title("📊 Learning Dashboard")

# Sidebar filters
st.sidebar.header("Filter by")
program_filter = st.sidebar.multiselect("Select Program:", df['Program Name'].unique(), default=df['Program Name'].unique())
department_filter = st.sidebar.multiselect("Select Department:", df['Department'].unique(), default=df['Department'].unique())
date_range = st.sidebar.date_input("Select Date Range:", [])

# Filter data
filtered_df = df[(df['Program Name'].isin(program_filter)) & (df['Department'].isin(department_filter))]
if date_range:
    filtered_df = filtered_df[(pd.to_datetime(df['Training Date']) >= pd.to_datetime(date_range[0])) & (pd.to_datetime(df['Training Date']) <= pd.to_datetime(date_range[1]))]

# KPI Cards
st.metric("Total Participants", len(filtered_df))
st.metric("Average Completion %", round(filtered_df['Completion %'].mean(), 2))
st.metric("Average Feedback Score", round(filtered_df['Feedback Score'].mean(), 2))

# Charts
st.subheader("📈 Program Completion % by Department")
completion_chart = px.bar(filtered_df, x='Department', y='Completion %', color='Program Name', barmode='group')
st.plotly_chart(completion_chart)

st.subheader("🎓 Quiz Scores Distribution")
quiz_chart = px.histogram(filtered_df, x='Quiz Score', nbins=10, color='Program Name')
st.plotly_chart(quiz_chart)

st.subheader("📅 Hours Spent per Participant")
hours_chart = px.scatter(filtered_df, x='Name', y='Hours Spent', color='Program Name', size='Hours Spent', hover_data=['Department'])
st.plotly_chart(hours_chart)

st.subheader("🎂 Completion by Program")
completion_pie = px.pie(filtered_df, names='Program Name', values='Completion %', title='Completion Distribution by Program')
st.plotly_chart(completion_pie)

# Participant Risk Level
st.subheader("⚠️ Participants at Risk")
risk_df = filtered_df[filtered_df['Completion %'] < 50]
st.write(risk_df[['Name', 'Department', 'Program Name', 'Completion %']])

# Display Data
st.subheader("📄 Dataset Overview")
st.dataframe(filtered_df)

# Export filtered dataset
st.download_button("📤 Export Filtered Data", data=filtered_df.to_csv(index=False), file_name="filtered_learning_dashboard.csv", mime="text/csv")

st.write("---")
st.write("💡 This dashboard helps visualize participant progress, engagement, and feedback across different learning programs.")
