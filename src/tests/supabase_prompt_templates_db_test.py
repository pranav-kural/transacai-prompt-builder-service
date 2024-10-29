import unittest
from unittest.mock import patch, MagicMock

from supabase import Client
from prompts.supabase_prompt_templates_db import SupabasePromptTemplatesDB

test_client_prompt_1_text = "test_prompt: {transactions}"

class TestSupabasePromptTemplatesDB(unittest.TestCase):

    @patch('prompts.supabase.client.get_supabase_client')
    def setUp(self, mock_get_supabase_client):
        self.mock_supabase_client = MagicMock()
        mock_get_supabase_client.return_value = self.mock_supabase_client
        self.db = SupabasePromptTemplatesDB()

    @patch('logger.utils.log_info')
    @patch('logger.utils.log_warning')
    def test_get_prompt_template_by_id_success(self, mock_log_warning, mock_log_info):
        # Mock the response from supabase client
        self.mock_supabase_client.table.return_value.select.return_value.eq.return_value.eq.return_value.execute.return_value.data = [{"prompt_text": test_client_prompt_1_text}]

        result = self.db.get_prompt_template_by_id("req_1", "test_client", 1)
        self.assertEqual(result, test_client_prompt_1_text)
        mock_log_warning.assert_not_called()

    @patch('logger.utils.log_info')
    @patch('logger.utils.log_warning')
    def test_get_prompt_template_by_id_not_found(self, mock_log_warning, mock_log_info):
        # Mock the response from supabase client
        self.mock_supabase_client.table.return_value.select.return_value.eq.return_value.eq.return_value.execute.return_value.data = []

        result = self.db.get_prompt_template_by_id("req123", "client123", 1)
        self.assertIsNone(result)

    @unittest.expectedFailure
    @patch('logger.utils.log_info')
    @patch('logger.utils.log_warning')
    def test_get_prompt_template_by_id_exception(self, mock_log_warning, mock_log_info):
        # Mock the response from supabase client to raise an exception
        self.db.supabase_client = Client("gg", "gg")

        with self.assertRaises(Exception) as context:
            self.db.get_prompt_template_by_id("req123", "client123", 1)
        self.assertTrue("Error while fetching prompt template" in str(context.exception))
        mock_log_warning.assert_called()

if __name__ == '__main__':
    unittest.main()