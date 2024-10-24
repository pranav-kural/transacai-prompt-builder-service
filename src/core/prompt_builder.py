from records.records_db import get_primary_records_db
from records.records_db_types import RecordsDBType
from prompts.prompt_templates_db import get_primary_prompt_templates_db
from prompts.prompt_templates_db_types import PromptTemplatesDBType

def build_prompt(req_id, client_id, prompt_id, from_time, to_time):
    # log
    print(f"Building prompt for request {req_id} with client {client_id} and prompt {prompt_id} for time period {from_time} to {to_time}")
    # get records
    primaryRecordsDB = get_primary_records_db(db_type=RecordsDBType.IN_MEMORY)
    records = primaryRecordsDB.get_records(req_id, client_id, from_time, to_time)
    # get prompt template
    primaryPromptTemplatesDB = get_primary_prompt_templates_db(db_type=PromptTemplatesDBType.IN_MEMORY)
    prompt_template = primaryPromptTemplatesDB.get_prompt_template_by_id(req_id, client_id, prompt_id)
    # build prompt
    return prompt_template.format(transactions=records)