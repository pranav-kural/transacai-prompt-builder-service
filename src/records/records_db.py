from logger.utils import log_error, log_info
from records.in_memory_records_db import InMemoryRecordsDB
from records.supabase_records_db import SupabaseRecordsDB
from records.primary_records_db import PrimaryRecordsDB
from records.records_db_types import RecordsDBType

# singleton instances to store primary instance of DB storing records data
in_memory_records_db: InMemoryRecordsDB | None = None
supabase_records_db: SupabaseRecordsDB | None = None

# method to get primary instance of DB storing records data (to support polymorphism)
def get_primary_records_db(db_type: RecordsDBType) -> PrimaryRecordsDB:
    """
    Method to get primary instance of DB storing records data depending on the type of DB provided.

    Args:
    db_type (RecordsDBType): Type of DB to get

    Returns:
    PrimaryRecordsDB: Instance of DB storing records data
    """
    log_info("get_primary_records_db - Getting primary records DB")
    global in_memory_records_db
    global supabase_records_db

    if db_type == RecordsDBType.IN_MEMORY:
        if in_memory_records_db is None:
            log_info("get_primary_records_db - db not initialized. Creating InMemoryRecordsDB instance")
            in_memory_records_db = InMemoryRecordsDB()
        return in_memory_records_db
    
    elif db_type == RecordsDBType.SUPABASE:
        if supabase_records_db is None:
            log_info("get_primary_records_db - db not initialized. Creating SupabaseRecordsDB instance")
            supabase_records_db = SupabaseRecordsDB()
        return supabase_records_db
    
    else:
        log_error("get_primary_records_db - Invalid DB type provided while getting primary records DB")
        raise Exception("Invalid DB type")