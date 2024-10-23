from src.prompts.primary_prompt_templates_db import PrimaryPromptTemplatesDB
from src.prompts.prompt_templates_db_types import PromptTemplatesDBType
from src.prompts.in_memory_prompt_templates_db import InMemoryPromptTemplatesDB

# Global variable to store primary instance of DB storing prompt templates data
db: PrimaryPromptTemplatesDB = None

# Method to get primary instance of DB storing prompt templates data (to support polymorphism)
# Follows the Singleton pattern to ensure only one instance of the DB is created
def get_primary_prompt_templates_db(db_type: PromptTemplatesDBType) -> PrimaryPromptTemplatesDB:
    global db
    if db is None:
        if db_type == PromptTemplatesDBType.IN_MEMORY:
            self.db = InMemoryPromptTemplatesDB()
        else:
            raise Exception("Invalid DB type")
    return db