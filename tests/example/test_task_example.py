from tests.example.task_examples import Extract


class TestBasicTasks:
    def test_extract_example_returns_10(self):
        extract_example = Extract()
        expected_result = 10

        task_result = extract_example.run()

        assert task_result == expected_result
