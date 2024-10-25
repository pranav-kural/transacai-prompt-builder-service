from enum import Enum

# Enum to define types of DB storing records data
class RecordsDBType(Enum):
    IN_MEMORY = "in_memory"

# Utility method to get RecordsDBType from string
def get_records_db_type_from_str(db_type: str) -> RecordsDBType:
    # Check if the given string is a valid RecordsDBType
    if not is_valid_records_db_type(db_type):
        raise ValueError(f"Invalid RecordsDBType: {db_type}")
    return RecordsDBType[db_type]

# Method to check if a given string is a valid RecordsDBType
# Possible values: "in_memory"
def is_valid_records_db_type(db_type: str) -> bool:
    return db_type in RecordsDBType.__members__