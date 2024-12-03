import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set the page configuration (this should be the first command in your script)
st.set_page_config(page_title="Task Management Dashboard", page_icon="✅", layout="wide")

# Load custom CSS
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

if 'page' not in st.session_state:
    st.session_state.page = "view_tasks"  # Default page

# Functions
def add_task(task_name, status, deadline, sub_tasks=[]):
    # Automatically set priority based on deadline
    today = datetime.today().date()
    if deadline <= today:
        priority = "High"
    elif deadline <= today + timedelta(days=3):
        priority = "Medium"
    else:
        priority = "Low"

    task = {
        'task_name': task_name,
        'priority': priority,
        'status': status,
        'deadline': deadline,
        'created_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'sub_tasks': sub_tasks  # New field for sub-tasks
    }
    st.session_state.tasks.append(task)
    st.success(f'Task "{task_name}" added successfully.')

def mark_as_completed(task_name):
    for task in st.session_state.tasks:
        if task['task_name'] == task_name:
            task['status'] = "Completed"
            st.success(f'Task "{task_name}" marked as completed.')

def edit_task(task_name, new_name, new_status, new_deadline, new_sub_tasks):
    for task in st.session_state.tasks:
        if task['task_name'] == task_name:
            task['task_name'] = new_name
            task['status'] = new_status
            task['deadline'] = new_deadline
            task['sub_tasks'] = new_sub_tasks
            st.success(f'Task "{task_name}" has been updated to "{new_name}".')

def calculate_task_progress(sub_tasks):
    completed_sub_tasks = len([sub_task for sub_task in sub_tasks if sub_task['status'] == 'Completed'])
    total_sub_tasks = len(sub_tasks)
    if total_sub_tasks == 0:
        return 0
    return (completed_sub_tasks / total_sub_tasks) * 100

def show_tasks():
    if len(st.session_state.tasks) > 0:
        task_df = pd.DataFrame(st.session_state.tasks)
        task_df['created_on'] = pd.to_datetime(task_df['created_on'])
        task_df['deadline'] = pd.to_datetime(task_df['deadline'])

        # Task table with search and filter
        st.write('<div class="section-heading">Current Tasks</div>', unsafe_allow_html=True)
        
        # Search bar
        search_term = st.text_input("Search Tasks", "")
        if search_term:
            task_df = task_df[task_df['task_name'].str.contains(search_term, case=False)]
        
        # Filter tasks by status and priority
        status_filter = st.selectbox("Filter by Status", ["All", "Not Started", "In Progress", "Completed"])
        if status_filter != "All":
            task_df = task_df[task_df['status'] == status_filter]
        
        priority_filter = st.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])
        if priority_filter != "All":
            task_df = task_df[task_df['priority'] == priority_filter]

        st.dataframe(task_df, width=1200)
    else:
        st.write("No tasks added yet.")

def show_task_progress():
    if len(st.session_state.tasks) > 0:
        task_df = pd.DataFrame(st.session_state.tasks)
        task_summary = task_df.groupby('priority').size().reset_index(name='count')

        # Task progress chart
        st.write('<div class="section-heading">Task Progress by Priority</div>', unsafe_allow_html=True)
        plt.figure(figsize=(4, 2))  # Smaller size for bar chart
        sns.barplot(x='priority', y='count', data=task_summary, palette='Set1')
        plt.title('Task Distribution by Priority', fontsize=10)  # Smaller title
        plt.ylabel('Number of Tasks', fontsize=8)  # Smaller labels
        st.pyplot(plt)

        # Pie chart for task status
        task_status_summary = task_df.groupby('status').size().reset_index(name='count')
        st.write('<div class="section-heading">Task Status Distribution</div>', unsafe_allow_html=True)
        plt.figure(figsize=(3, 3))  # Small size for pie chart
        plt.pie(task_status_summary['count'], labels=task_status_summary['status'], autopct='%1.1f%%', startangle=140)
        plt.title('Task Progress by Status', fontsize=10)  # Smaller title
        st.pyplot(plt)
    else:
        st.write("No tasks to display progress.")

def manage_task():
    # Manage tasks (Mark as completed and Edit Task)
    st.write('<div class="section-heading">Manage Task</div>', unsafe_allow_html=True)
    
    # Mark task as completed
    with st.expander("Mark Task as Completed"):
        task_to_complete = st.selectbox("Select a task", [task['task_name'] for task in st.session_state.tasks])
        if st.button("Mark as Completed"):
            mark_as_completed(task_to_complete)
    
    # Edit Task
    with st.expander("Edit Task"):
        task_to_edit = st.selectbox("Select a task to edit", [task['task_name'] for task in st.session_state.tasks])
        new_task_name = st.text_input("New Task Name", task_to_edit)
        new_status = st.selectbox("New Status", ["Not Started", "In Progress", "Completed"])
        new_deadline = st.date_input("New Deadline", min_value=datetime.today().date())
        new_sub_tasks = []
        
        num_sub_tasks = st.number_input("Number of Sub-Tasks", min_value=0, max_value=10)
        for i in range(num_sub_tasks):
            sub_task_name = st.text_input(f"Sub-Task {i+1} Name")
            sub_task_status = st.selectbox(f"Sub-Task {i+1} Status", ["Not Started", "In Progress", "Completed"])
            new_sub_tasks.append({'name': sub_task_name, 'status': sub_task_status})
        
        if st.button("Update Task"):
            edit_task(task_to_edit, new_task_name, new_status, new_deadline, new_sub_tasks)

# Sidebar Navigation
st.sidebar.title("Task Dashboard")
if st.sidebar.button("Add Task"):
    st.session_state.page = "add_task"
if st.sidebar.button("View Tasks"):
    st.session_state.page = "view_tasks"
if st.sidebar.button("Task Progress"):
    st.session_state.page = "task_progress"
if st.sidebar.button("Manage Task"):
    st.session_state.page = "manage_task"

# Page Content
if st.session_state.page == "add_task":
    st.write('<div class="section-heading">Add New Task</div>', unsafe_allow_html=True)
    with st.form(key='task_form', clear_on_submit=True):
        task_name = st.text_input("Task Name", key="task_name", max_chars=50)
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"], key="status")
        deadline = st.date_input("Deadline", min_value=datetime.today().date(), key="deadline")
        submit_button = st.form_submit_button("Add Task")

        if submit_button:
            add_task(task_name, status, deadline)

elif st.session_state.page == "view_tasks":
    show_tasks()

elif st.session_state.page == "task_progress":
    show_task_progress()

elif st.session_state.page == "manage_task":
    manage_task()
