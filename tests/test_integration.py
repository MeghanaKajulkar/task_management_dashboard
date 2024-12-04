import pytest
from datetime import datetime
import streamlit as st
from utils.task_functions import add_task, mark_as_completed, show_tasks

def test_add_and_mark_task_completed():
    # Mock session_state
    st.session_state.tasks = []

    # Add a task
    task_name = "Test Task"
    status = "Not Started"
    deadline = datetime(2024, 12, 15).date()

    # Add the task using add_task function
    add_task(task_name, status, deadline)

    # Now, mark the task as completed using the mark_as_completed function
    mark_as_completed(task_name)

    # Check if the task's status has been updated to "Completed"
    assert len(st.session_state.tasks) == 1  # Task should still be in session_state
    assert st.session_state.tasks[0]["status"] == "Completed"  # The status should be updated to "Completed"
    assert st.session_state.tasks[0]["task_name"] == task_name  # The task name should remain the same

