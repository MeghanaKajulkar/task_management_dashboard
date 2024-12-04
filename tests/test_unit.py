import pytest
from datetime import datetime, timedelta
import streamlit as st
from utils.task_functions import add_task

# Fixture to initialize session state for each test
@pytest.fixture(autouse=True)
def mock_session_state():
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

def test_add_task_high_priority():
    """Test adding a task with a high priority (deadline within 3 days)."""
    task_name = "Urgent Task"
    status = "Not Started"
    deadline = datetime.today().date() + timedelta(days=2)  # Deadline within 3 days
    
    add_task(task_name, status, deadline)
    
    # Verify that the task was added and the priority is 'High'
    assert len(st.session_state['tasks']) == 1
    assert st.session_state['tasks'][0]['task_name'] == task_name
    assert st.session_state['tasks'][0]['priority'] == "High"

def test_add_task_medium_priority():
    """Test adding a task with a medium priority (deadline between 4-7 days)."""
    task_name = "Important Task"
    status = "Not Started"
    deadline = datetime.today().date() + timedelta(days=5)  # Deadline between 4-7 days
    
    add_task(task_name, status, deadline)
    
    # Verify that the task was added and the priority is 'Medium'
    assert len(st.session_state['tasks']) == 1
    assert st.session_state['tasks'][0]['task_name'] == task_name
    assert st.session_state['tasks'][0]['priority'] == "Medium"

def test_add_task_low_priority():
    """Test adding a task with a low priority (deadline more than 7 days)."""
    task_name = "Long-term Task"
    status = "Not Started"
    deadline = datetime.today().date() + timedelta(days=10)  # Deadline more than 7 days
    
    add_task(task_name, status, deadline)
    
    # Verify that the task was added and the priority is 'Low'
    assert len(st.session_state['tasks']) == 1
    assert st.session_state['tasks'][0]['task_name'] == task_name
    assert st.session_state['tasks'][0]['priority'] == "Low"
