import requests
from supabase_py import create_client, Client

#url: str = os.environ.get("SUPABASE_URL")
#key: str = os.environ.get("SUPABASE_KEY")
#sb: Client = create_client(url, key)

# Supabase project details
sb_url: str = 'https://hlmyhwperjzxvtfhdbkw.supabase.co'
sb_key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsbXlod3Blcmp6eHZ0ZmhkYmt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTYxMTk0NTcsImV4cCI6MjAxMTY5NTQ1N30.bHzzlJycNv_PWk_s7_PEvYY3HPqRbf83TrnklLAVMYk'

sb: Client = create_client(sb_url, sb_key)

# supbabase package stuff
#sb = create_client(sb_url, sb_key)

# Function to send data to Supabase

data = {'id': 1, 'temp': 35.452, 'moist': 60}

try:
    # Insert data into the Supabase table
    insert_data = sb.table('time_temp_humidity_1').insert(data).execute()
    response_message = "Data added successfully"
except Exception as e:
    response_message = f"Error: {str(e)}"

print(response_message)
