from prefect.core.edge import Edge

from tests.example.job_examples import basic_test_flow, extract_example, transform_example, load_example

class TestBasicFlow:
    def test_basic_flow_composition(self):
        expected_tasks = {extract_example, transform_example, load_example}
        expected_edges = {Edge(extract_example, transform_example, "x"), Edge(transform_example, load_example, "y")}

        assert basic_test_flow.tasks == expected_tasks
        assert basic_test_flow.edges == expected_edges

        # check flow starting and termination points
        assert basic_test_flow.root_tasks() == set([extract_example])
        assert basic_test_flow.terminal_tasks() == set([load_example])

    def test_basic_flow_task_status(self):
        state = basic_test_flow.run()

        assert state.is_successful()
        assert state.result[extract_example].is_successful()
        assert state.result[transform_example].is_successful()
        assert state.result[load_example].is_successful()

    def test_basic_flow_task_results(self):        
        state = basic_test_flow.run()

        assert state.is_successful()
        assert state.result[extract_example].result == 10
        assert state.result[transform_example].result == 20
        assert state.result[load_example].result == None
