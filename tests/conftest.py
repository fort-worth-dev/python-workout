"""
Shared pytest fixtures for Python Workout tests.

This module contains fixtures that can be used across all test modules.
"""


import pytest


@pytest.fixture
def sample_numbers():
    """Provide a list of sample numbers for testing."""
    return [1, 2, 3, 4, 5, 10, 20, 100]


@pytest.fixture
def sample_strings():
    """Provide a list of sample strings for testing."""
    return ["hello", "world", "python", "workout"]


@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing file operations."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Sample content\nLine 2\nLine 3\n")
    return file_path


@pytest.fixture
def sample_data_dict():
    """Provide a sample dictionary for testing."""
    return {
        "name": "Test User",
        "age": 30,
        "email": "test@example.com",
        "active": True,
    }
