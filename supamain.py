import os
from supabase import create_client, Client
from dotenv import load_dotenv

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

print(url,key)
#supabase: Client = create_client(url, key)