import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from config.css import custom_css
from utils.task_functions import add_task, mark_as_completed, show_tasks, show_task_progress, manage_task  # Import manage_task function

# Set the page configuration
st.set_page_config(page_title="Task Management", page_icon="✅", layout="wide")

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if 'page' not in st.session_state:
    st.session_state.page = "view_tasks"  # Default page

# Sidebar Navigation
st.sidebar.title("Task Dashboard")
if st.sidebar.button("Add Task"):
    st.session_state.page = "add_task"
if st.sidebar.button("View Tasks"):
    st.session_state.page = "view_tasks"
if st.sidebar.button("Task Progress"):
    st.session_state.page = "task_progress"
if st.sidebar.button("Manage Task"):  # Add back "Manage Task"
    st.session_state.page = "manage_task"  # Switch to the "manage_task" page

# Page Content
if st.session_state.page == "add_task":
    st.write('<div class="section-heading">Add New Task</div>', unsafe_allow_html=True)
    with st.form(key='task_form', clear_on_submit=True):
        task_name = st.text_input("Task Name", max_chars=50)
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
        deadline = st.date_input("Deadline", min_value=datetime.today().date())
        submit_button = st.form_submit_button("Add Task")

        if submit_button:
            add_task(task_name, status, deadline)

elif st.session_state.page == "view_tasks":
    show_tasks()

elif st.session_state.page == "task_progress":
    show_task_progress()

elif st.session_state.page == "manage_task":  # Add logic for "Manage Task" page
    manage_task()  # Call the function to manage tasks
