from prefect import Client

from tests.example.job_examples import basic_test_flow
from src.flows import combine_enim_accidents_with_ship_flow

project_name = "setup_project"
prefect_client = Client()
prefect_client.create_project(project_name=project_name)

flows_to_register = (
    basic_test_flow,
    combine_enim_accidents_with_ship_flow,
)

for flow in flows_to_register:
    flow.register(project_name=project_name)
