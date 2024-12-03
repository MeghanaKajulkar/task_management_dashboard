import pytest
from datetime import datetime
from utils.task_functions import add_task

def test_add_task():
    task_list = []
    add_task("Test Task", "Not Started", datetime.today().date())
    assert len(task_list) == 1
