import pytest
import subprocess
import time
import requests
from datetime import datetime

# Start the app in a subprocess for testing
@pytest.fixture(scope="module")
def start_streamlit_app():
    # Start the Streamlit app
    process = subprocess.Popen(
        ["streamlit", "run", "app.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(5)  # Allow some time for the app to start
    yield
    process.terminate()

def test_add_task(start_streamlit_app):
    """Test adding a task to the dashboard."""
    url = "http://localhost:8501"  # Default Streamlit app URL
    response = requests.get(url)
    assert response.status_code == 200, "Streamlit app did not start correctly."

    # Add logic for interacting with the app if possible

def test_task_progress_chart_render(start_streamlit_app):
    """Test if the task progress chart renders correctly."""
    url = "http://localhost:8501/task_progress"  # Adjust based on app routing
    response = requests.get(url)
    assert response.status_code == 200, "Task Progress page did not render correctly."

    # Further validation could be done by parsing HTML or JSON responses
