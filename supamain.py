import os
from supabase import create_client, Client
from dotenv import load_dotenv
import time


load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Create a random user login email and password.
random_email: str = "axel.k.ingo@gmail.com"
random_password: str = "Pass2"
random_data = {"email":"em123?","password":"pw2022?"}

def sign_up(email, pw):
    user = supabase.auth.sign_up(email=email, password=pw)
    return user

def sign_in(email, pw):
    user = supabase.auth.sign_in(email=email, password=pw)
    return user

def insert_data(tblName,tblData):
    data = supabase.table(table_name=tblName).insert(tblData).execute()
    assert len(data.data) > 0

def get_data(tblName):
    data = supabase.table(table_name=tblName).select("*").execute()
    return data

#active_user = sign_up(random_email,random_password)
time.sleep(2)
active_user = sign_in(random_email,random_password)
#print(active_user.id)

time.sleep(2)
#insert_data("test-table",random_data)
data = get_data("test-table")
print(type(data))