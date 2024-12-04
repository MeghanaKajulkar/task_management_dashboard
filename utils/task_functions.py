import streamlit as st
import pandas as pd
from datetime import datetime

def add_task(task_name, status, deadline):
    priority = "High" if deadline < datetime.today().date() else "Medium"
    task = {
        'task_name': task_name,
        'priority': priority,
        'status': status,
        'deadline': deadline,
        'created_on': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.tasks.append(task)
    st.success(f'Task "{task_name}" added successfully.')

def mark_as_completed(task_name):
    for task in st.session_state.tasks:
        if task['task_name'] == task_name:
            task['status'] = "Completed"
            st.success(f'Task "{task_name}" marked as completed.')

def show_tasks():
    if len(st.session_state.tasks) > 0:
        task_df = pd.DataFrame(st.session_state.tasks)
        task_df['created_on'] = pd.to_datetime(task_df['created_on'])
        task_df['deadline'] = pd.to_datetime(task_df['deadline'])

        st.write('<div class="section-heading">Current Tasks</div>', unsafe_allow_html=True)
        st.dataframe(task_df, width=1200)

        with st.expander("Mark Task as Completed"):
            task_to_complete = st.selectbox("Select a task", task_df['task_name'])
            if st.button("Mark as Completed"):
                mark_as_completed(task_to_complete)
    else:
        st.write("No tasks added yet.")

def show_task_progress():
    if len(st.session_state.tasks) > 0:
        task_df = pd.DataFrame(st.session_state.tasks)
        task_summary = task_df.groupby('priority').size().reset_index(name='count')

        st.write('<div class="section-heading">Task Progress by Priority</div>', unsafe_allow_html=True)
        plt.figure(figsize=(6, 3))
        sns.barplot(x='priority', y='count', data=task_summary, palette='Set1')
        plt.title('Task Distribution by Priority')
        plt.ylabel('Number of Tasks')
        st.pyplot(plt)

        task_status_summary = task_df.groupby('status').size().reset_index(name='count')
        st.write('<div class="section-heading">Task Status Distribution</div>', unsafe_allow_html=True)
        plt.figure(figsize=(4, 4))
        plt.pie(task_status_summary['count'], labels=task_status_summary['status'], autopct='%1.1f%%', startangle=140)
        plt.title('Task Progress by Status')
        st.pyplot(plt)
    else:
        st.write("No tasks to display progress.")

# Function to edit tasks (name, status, deadline, etc.)
def edit_task(task_name, new_name, new_status, new_deadline):
    for task in st.session_state.tasks:
        if task['task_name'] == task_name:
            task['task_name'] = new_name
            task['status'] = new_status
            task['deadline'] = new_deadline
            st.success(f'Task "{task_name}" has been updated to "{new_name}".')

# Function to manage tasks (mark as completed or edit)
def manage_task():
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
        if st.button("Update Task"):
            edit_task(task_to_edit, new_task_name, new_status, new_deadline)
