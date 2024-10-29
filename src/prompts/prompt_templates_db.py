from logger.utils import log_error, log_info
from prompts.primary_prompt_templates_db import PrimaryPromptTemplatesDB
from prompts.prompt_templates_db_types import PromptTemplatesDBType
from prompts.in_memory_prompt_templates_db import InMemoryPromptTemplatesDB
from prompts.supabase_prompt_templates_db import SupabasePromptTemplatesDB

# Singleton instances to store DBs for storing prompt templates data
in_memory_prompt_templates_db: InMemoryPromptTemplatesDB | None = None
supabase_prompt_templates_db: SupabasePromptTemplatesDB | None = None

# Method to get a singleton instance of DB storing prompt templates data
# Follows the Singleton pattern to ensure only one instance of the DB is created
def get_primary_prompt_templates_db(db_type: PromptTemplatesDBType) -> PrimaryPromptTemplatesDB:
    """
    Method to get an instance of DB storing prompt templates data depending on the type of DB provided.

    Args:
    db_type (PromptTemplatesDBType): Type of DB to get

    Returns:
    PrimaryPromptTemplatesDB: Instance of DB storing prompt templates data
    """
    log_info("get_primary_prompt_templates_db - Getting primary prompt templates DB")
    global in_memory_prompt_templates_db
    global supabase_prompt_templates_db

    if db_type == PromptTemplatesDBType.IN_MEMORY:
        if in_memory_prompt_templates_db is None:
            log_info("get_primary_prompt_templates_db - Creating InMemoryPromptTemplatesDB")
            in_memory_prompt_templates_db = InMemoryPromptTemplatesDB()
        return in_memory_prompt_templates_db
    
    elif db_type == PromptTemplatesDBType.SUPABASE:
        if supabase_prompt_templates_db is None:
            log_info("get_primary_prompt_templates_db - Creating SupabasePromptTemplatesDB")
            supabase_prompt_templates_db = SupabasePromptTemplatesDB()
        return supabase_prompt_templates_db
    
    else:
        log_error("get_primary_prompt_templates_db - Invalid DB type")
        raise Exception("Invalid DB type")