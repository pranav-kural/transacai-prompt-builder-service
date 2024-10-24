from prompts.primary_prompt_templates_db import PrimaryPromptTemplatesDB
from prompts.prompt_templates_db_types import PromptTemplatesDBType
from prompts.in_memory_prompt_templates_db import InMemoryPromptTemplatesDB

# Global variable to store primary instance of DB storing prompt templates data
db: PrimaryPromptTemplatesDB = None

# Method to get primary instance of DB storing prompt templates data (to support polymorphism)
# Follows the Singleton pattern to ensure only one instance of the DB is created
def get_primary_prompt_templates_db(db_type: PromptTemplatesDBType) -> PrimaryPromptTemplatesDB:
    global db
    if db is None:
        if db_type == PromptTemplatesDBType.IN_MEMORY:
            db = InMemoryPromptTemplatesDB()
        else:
            raise Exception("Invalid DB type")
    return db