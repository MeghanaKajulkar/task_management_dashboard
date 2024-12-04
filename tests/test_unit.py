import pytest
import streamlit as st
from datetime import datetime
from utils.task_functions import add_task

@pytest.fixture(autouse=True)
def mock_session_state():
    if 'tasks' not in st.session_state:
        st.session_state['tasks'] = []

def test_add_task():
    """Test adding a task to the session state."""
    add_task("Test Task", "Not Started", datetime.today().date())
    
    # Verify that the task was added
    assert len(st.session_state['tasks']) == 1
    assert st.session_state['tasks'][0]['task_name'] == "Test Task"
    assert st.session_state['tasks'][0]['status'] == "Not Started"
    assert st.session_state['tasks'][0]['priority'] == "Medium"  # Assuming the date is in the future
