import os
from supabase import create_client, Client

url: str = os.environ.get("SPB_URL")
key: str = os.environ.get("SPB_KEY")

print(url,key)
#supabase: Client = create_client(url, key)