import pytest
import streamlit as st
from utils.task_functions import add_task

def test_add_task():
    # Mock session_state
    st.session_state.tasks = []

    # Input data
    task_name = "Test Task"
    status = "Not Started"
    deadline = "2024-12-15"

    # Call the function to add the task
    add_task(task_name, status, deadline)

    # Check if the task was added
    assert len(st.session_state.tasks) == 1
    assert st.session_state.tasks[0]["task_name"] == task_name
