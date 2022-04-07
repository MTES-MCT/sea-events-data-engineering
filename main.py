from prefect import Client

from tests.example.job_examples import basic_test_flow

project_name = "setup_project"
prefect_client = Client()
prefect_client.create_project(project_name=project_name)

basic_test_flow.register(
    project_name=project_name
)
