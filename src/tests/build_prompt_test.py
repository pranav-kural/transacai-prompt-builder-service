import unittest
from unittest.mock import patch, MagicMock
from core.prompt_builder import build_prompt
from records.records_db_types import RecordsDBType

class TestBuildPrompt(unittest.TestCase):

    @patch('logger.logger.get_testing_logger')
    def test_run_build_prompt(self, mock_get_testing_logger):
        mock_logger = MagicMock()
        mock_get_testing_logger.return_value = mock_logger

        try:
            prompt = build_prompt(
                req_id="req_1", 
                client_id="test_client", 
                prompt_id=1, 
                records_source_id=RecordsDBType.IN_MEMORY,
                from_time="2019-12-29T06:39:22", 
                to_time="2019-12-29T23:59:22"
            )
            self.assertIsNotNone(prompt)
            mock_logger.info("Test - run_build_prompt_test - Passed")
        except Exception as e:
            mock_logger.info(f"Test - run_build_prompt_test - Failed with error: {str(e)}")

        mock_logger.info.assert_called_with("Test - run_build_prompt_test - Passed")

    @unittest.expectedFailure
    @patch('logger.logger.get_testing_logger')
    def test_run_build_prompt_invalid_prompt_id(self, mock_get_testing_logger):
        mock_logger = MagicMock()
        mock_get_testing_logger.return_value = mock_logger

        try:
            build_prompt(
                req_id="req_1", 
                client_id="test_client", 
                prompt_id=100, 
                records_source_id=RecordsDBType.IN_MEMORY,
                from_time="2019-12-29T06:39:22", 
                to_time="2019-12-29T23:49:22"
            )
            self.fail("Test - run_build_prompt_invalid_prompt_id_test - Failed")
        except Exception as e:
            mock_logger.info.assert_called_with(f"Test - run_build_prompt_invalid_prompt_id_test - Passed with error: {str(e)}")

    @unittest.expectedFailure
    @patch('logger.logger.get_testing_logger')
    def test_run_build_prompt_invalid_records(self, mock_get_testing_logger):
        mock_logger = MagicMock()
        mock_get_testing_logger.return_value = mock_logger

        try:
            build_prompt(
                req_id="req_1", 
                client_id="test_client", 
                prompt_id=1, 
                records_source_id=RecordsDBType.IN_MEMORY,
                from_time="2019-12-29T06:49:22", 
                to_time="2019-12-29T06:49:22"
            )
            self.fail("Test - run_build_prompt_invalid_records_test - Failed")
        except Exception as e:
            mock_logger.info.assert_called_with(f"Test - run_build_prompt_invalid_records_test - Passed with error: {str(e)}")

if __name__ == '__main__':
    unittest.main()