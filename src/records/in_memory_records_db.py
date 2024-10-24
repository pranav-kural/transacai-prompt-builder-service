import pandas as pd
from logger.utils import log_info, log_warning
from records.primary_records_db import PrimaryRecordsDB

# Class representing an in-memory database of records
class InMemoryRecordsDB(PrimaryRecordsDB):

  filename = "transac_sample_v1.csv"

  def __init__(self):
    log_info("Initializing InMemoryRecordsDB for file: " + self.filename)
    # load data
    self.data = pd.read_csv(self.filename)

  # method to get records given request id, client id, from_time and to_time
  def get_records(self, req_id: str, client_id: str, from_time: str, to_time: str) -> str | None:
    """
    Method to get records given request id, client id, from_time and to_time.

    Args:
    req_id (string): Request ID
    client_id (string): Client ID
    from_time (datetime): Start time of time period
    to_time (datetime): End time of time period

    Returns:
    records (Array): Array of records
    """
    log_info(f"get_records - Getting records for request {req_id} with client {client_id} for time period {from_time} to {to_time}")
    # return records where completed_at is between from_time and to_time
    result: pd.DataFrame | None = self.data[(self.data["completed_at"] >= from_time) & (self.data["completed_at"] <= to_time)]
    # if result set not empty, return records as list of strings with first row as column names
    if result is not None and not result.empty:
      return result.to_json(orient="records")
    else:
      log_warning(f"get_records - No records found for request {req_id} with client {client_id} for time period {from_time} to {to_time}")
      return None