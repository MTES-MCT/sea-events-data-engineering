################
# Example jobs #
################
from prefect import Flow

from tests.example.task_examples import Extract, Transform, Load

basic_test_flow = Flow("testing-example")
extract_example = Extract()
transform_example = Transform()
load_example = Load()

basic_test_flow.add_edge(upstream_task=extract_example, downstream_task=transform_example, key="x")
basic_test_flow.add_edge(upstream_task=transform_example, downstream_task=load_example, key="y")

