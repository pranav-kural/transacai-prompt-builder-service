from logger.utils import log_error, log_info
from records.records_db import get_primary_records_db
from records.records_db_types import RecordsDBType
from prompts.prompt_templates_db import get_primary_prompt_templates_db
from prompts.prompt_templates_db_types import PromptTemplatesDBType

def build_prompt(req_id: str, client_id: str, prompt_id: int, records_source_id: RecordsDBType, prompt_templates_source_id: PromptTemplatesDBType, from_time: str, to_time: str) -> str:
    """
    Method to build prompt for given request id, client id, prompt id and time period.

    Args:
    req_id (string): Request ID
    client_id (string): Client ID
    prompt_id (int): ID of prompt template to use
    records_source_id (RecordsDBType): ID of database to use for records
    prompt_templates_source_id (PromptTemplatesDBType): ID of database to use for prompt templates
    from_time (datetime): Start time of time period
    to_time (datetime): End time of time period

    Returns:
    prompt (string): Prompt string
    """
    log_info(f"build_prompt - Building prompt for request {req_id} with client {client_id} and prompt {prompt_id} for time period {from_time} to {to_time}")
    # get records
    primaryRecordsDB = get_primary_records_db(db_type=records_source_id)
    records = primaryRecordsDB.get_records(req_id, client_id, from_time, to_time)
    # validate records
    if not records:
        log_error(f"build_prompt - No records found for request {req_id} with client {client_id} for time period {from_time} to {to_time}")
        raise Exception("No records found for the given time period")
    # get prompt template
    primaryPromptTemplatesDB = get_primary_prompt_templates_db(db_type=prompt_templates_source_id)
    prompt_template = primaryPromptTemplatesDB.get_prompt_template_by_id(req_id, client_id, prompt_id)
    # validate prompt template
    if not prompt_template:
        log_error(f"build_prompt - No prompt template found for request {req_id} with client {client_id} and prompt {prompt_id}")
        raise Exception("No prompt template found for the given prompt id")
    # build prompt
    return prompt_template.format(transactions=records)