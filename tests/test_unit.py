import pytest
from datetime import datetime
import streamlit as st
from utils.task_functions import add_task

def test_add_and_view_task():
    # Mock session_state
    st.session_state.tasks = []
    
    # Add a task
    task_name = "Test Task"
    status = "Not Started"
    
    # Convert string to datetime.date
    deadline = datetime(2024, 12, 15).date()

    # Call the add_task function
    add_task(task_name, status, deadline)

    # Check if the task was added
    assert len(st.session_state.tasks) == 1
    assert st.session_state.tasks[0]["task_name"] == task_name
    assert st.session_state.tasks[0]["status"] == status
    assert st.session_state.tasks[0]["deadline"] == deadline
