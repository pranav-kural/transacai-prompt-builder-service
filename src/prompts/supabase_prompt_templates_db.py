from logger.utils import log_info, log_warning
from prompts.primary_prompt_templates_db import PrimaryPromptTemplatesDB
from vendors.supabase.client import get_supabase_client

# Supabase prompt templates store
class SupabasePromptTemplatesDB(PrimaryPromptTemplatesDB):
    # Initialize client
    def __init__(self):
        self.supabase_client = get_supabase_client()

    # method to get prompt template by id
    def get_prompt_template_by_id(self, req_id, client_id, prompt_id) -> str | None:
      """
      Method to get prompt template by id. Client ID must also be provided and match, i.e., prompt template must belong to the client.

      Args:
      req_id (string): Request ID
      client_id (string): Client ID
      prompt_id (int): Prompt ID

      Returns:
      prompt_template (Dict): Prompt template
      """
      log_info(f"get_prompt_template_by_id - Getting prompt template for request {req_id} with client {client_id} and prompt {prompt_id}")
      try:
          # fetch prompt template with given id and client id
          response = self.supabase_client.table("prompt_templates").select("prompt_text").eq("id", prompt_id).eq("client_id", client_id).execute()
      except Exception as e:
          log_warning(f"get_prompt_template_by_id - Error while fetching prompt template: {e}")
          raise Exception("Error while fetching prompt template")
      # validate response
      if response.data is None or len(response.data) == 0:
          log_warning(f"get_prompt_template_by_id - No prompt template found for request {req_id} with client {client_id} and prompt {prompt_id}")
          return None
      log_info(f"get_prompt_template_by_id - Prompt template found for request {req_id} with client {client_id} and prompt {prompt_id}")
      # return prompt template
      return response.data[0]["prompt_text"]