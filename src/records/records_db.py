from records.in_memory_records_db import InMemoryRecordsDB
from records.primary_records_db import PrimaryRecordsDB
from records.records_db_types import RecordsDBType

# singleton instance to store primary instance of DB storing records data
primary_records_db: PrimaryRecordsDB = None

# method to get primary instance of DB storing records data (to support polymorphism)
def get_primary_records_db(db_type: RecordsDBType) -> PrimaryRecordsDB:
    global primary_records_db
    if primary_records_db is None:
        if db_type == RecordsDBType.IN_MEMORY:
            primary_records_db = InMemoryRecordsDB()
        else:
            raise Exception("Invalid DB type")
    return primary_records_db