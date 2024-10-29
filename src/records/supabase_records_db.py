from logger.utils import log_info, log_warning
from records.primary_records_db import PrimaryRecordsDB
from vendors.supabase.client import get_supabase_client

# Class to access records stored in Supabase Postgres DB
class SupabaseRecordsDB(PrimaryRecordsDB):
    """
    Class to access records stored in Supabase Postgres DB
    """

    # Initialize client
    def __init__(self):
        self.supabase_client = get_supabase_client()

    # method to get records by request id, client id, from_time and to_time
    def get_records(self, req_id, client_id, from_time, to_time) -> str | None:
        """
        Method to get records by request id, client id, from_time and to_time

        Args:
        req_id (string): Request ID
        client_id (string): Client ID
        from_time (string): From time
        to_time (string): To time

        Returns:
        records (Dict): Records
        """
        log_info(f"get_records - Getting records for request {req_id} with client {client_id} from {from_time} to {to_time}")
        try:
            # fetch records with given request id, client id, from time and to time
            response = self.supabase_client.table("records").select("completed_at,merchant,category,amount,first,last,city,role,currency").eq("client_id", client_id).gte("completed_at", from_time).lte("completed_at", to_time).order("completed_at").execute()

            # validate response
            if response.data is None or len(response.data) == 0:
                log_warning(f"get_records - No records found for request {req_id} with client {client_id} from {from_time} to {to_time}")
                return None
            log_info(f"get_records - Records found for request {req_id} with client {client_id} from {from_time} to {to_time}")
            # return records as string
            return ''.join([str(record) for record in response.data])
        
        except Exception as e:
            log_warning(f"get_records - Error while fetching records: {e}")
            raise Exception("Error while fetching records")
        