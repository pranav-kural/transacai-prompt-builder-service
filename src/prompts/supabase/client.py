import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Singleton instance of supabase client
supabase: Client | None = None #create_client(url, key)

def get_supabase_client() -> Client:
    """
    Method to get the supabase client. If client is not initialized, it will be initialized using SUPABASE_URL and SUPABASE_KEY environment variables.

    Returns:
    supabase (Client): Supabase client
    """
    global supabase
    if supabase is None:
        url_text = os.environ.get("SUPABASE_URL")
        # validate url
        if url_text is None:
            raise Exception("SUPABASE_URL is not set")
        key_text = os.environ.get("SUPABASE_KEY")
        # validate key
        if key_text is None:
            raise Exception("SUPABASE_KEY is not set")
        # Initialize the supabase client
        supabase = create_client(url_text, key_text)
    return supabase
