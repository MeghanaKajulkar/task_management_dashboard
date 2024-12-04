import pytest
import streamlit as st
from utils.task_functions import add_task, show_tasks

def test_add_and_view_task():
    # Mock session_state
    st.session_state.tasks = []

    # Add a task
    task_name = "Test Task"
    add_task(task_name, "Not Started", "2024-12-15")

    # Verify task is added
    assert len(st.session_state.tasks) == 1
    assert st.session_state.tasks[0]["task_name"] == task_name

    # Simulate viewing tasks (just check if any task exists)
    show_tasks()
    assert "Test Task" in [task["task_name"] for task in st.session_state.tasks]

