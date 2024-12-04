import pytest
from datetime import datetime, timedelta
import streamlit as st
from utils.task_functions import add_task

@pytest.fixture(autouse=True)
def mock_session_state():
    """Mock the session state for Streamlit before each test."""
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []  # Initialize an empty list of tasks

def test_add_task_high_priority():
    """Test adding a task with a high priority (deadline within 3 days)."""
    task_name = "Urgent Task"
    status = "Not Started"
    deadline = datetime.today().date() + timedelta(days=2)  # Deadline within 3 days
    
    # Add the task
    add_task(task_name, status, deadline)
    
    # Check that the task was added with the correct priority (High)
    assert len(st.session_state['tasks']) == 1  # One task should be added
    assert st.session_state['tasks'][0]['priority'] == "High"  # Priority should be High
