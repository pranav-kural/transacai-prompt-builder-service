from enum import Enum

# Enum to define types of DB storing prompt templates data
class PromptTemplatesDBType(Enum):
    IN_MEMORY = "in_memory"
    SUPABASE = "supabase"

# Utility method to get PromptTemplatesDBType from string
def get_prompt_templates_db_type_from_str(db_type: str) -> PromptTemplatesDBType:
    # convert to UPPERCASE
    db_type = db_type.upper()
    # Check if the given string is a valid PromptTemplatesDBType
    if not is_valid_prompt_templates_db_type(db_type):
        raise ValueError(f"Invalid PromptTemplatesDBType: {db_type}")
    return PromptTemplatesDBType[db_type]

# Method to check if a given string is a valid PromptTemplatesDBType
def is_valid_prompt_templates_db_type(db_type: str) -> bool:
    return db_type in PromptTemplatesDBType.__members__