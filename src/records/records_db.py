from logger.utils import log_error, log_info
from records.in_memory_records_db import InMemoryRecordsDB
from records.primary_records_db import PrimaryRecordsDB
from records.records_db_types import RecordsDBType

# singleton instance to store primary instance of DB storing records data
primary_records_db: PrimaryRecordsDB | None = None

# method to get primary instance of DB storing records data (to support polymorphism)
def get_primary_records_db(db_type: RecordsDBType) -> PrimaryRecordsDB:
    log_info("get_primary_records_db - Getting primary records DB")
    global primary_records_db
    if primary_records_db is None:
        if db_type == RecordsDBType.IN_MEMORY:
            log_info("get_primary_records_db - db not initialized. Creating InMemoryRecordsDB instance")
            primary_records_db = InMemoryRecordsDB()
        else:
            log_error("get_primary_records_db - Invalid DB type provided while getting primary records DB")
            raise Exception("Invalid DB type")
    return primary_records_db