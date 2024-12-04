import pytest
import streamlit as st
from datetime import datetime
from utils.task_functions import add_task

@pytest.fixture(autouse=True)
def mock_session_state():
    """Fixture to mock the session state for testing."""
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []  # Initialize tasks as an empty list

def test_add_task():
    """Test adding a task to the dashboard."""
    # Simulate adding a task
    add_task("Test Task", "Not Started", datetime.today().date())
    
    # Verify that the task was added
    assert len(st.session_state['tasks']) == 1
    assert st.session_state['tasks'][0]['name'] == "Test Task"
    assert st.session_state['tasks'][0]['status'] == "Not Started"
