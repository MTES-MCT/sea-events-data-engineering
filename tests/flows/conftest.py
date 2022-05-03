import pytest
from src.repositories.repository_setup import repository_setup


@pytest.fixture
def reset_repository():
    repository_setup()
