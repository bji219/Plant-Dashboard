import requests
from supabase_py import create_client # , Client

# Supabase project details
sb_url = 'https://hlmyhwperjzxvtfhdbkw.supabase.co'
sb_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsbXlod3Blcmp6eHZ0ZmhkYmt3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTYxMTk0NTcsImV4cCI6MjAxMTY5NTQ1N30.bHzzlJycNv_PWk_s7_PEvYY3HPqRbf83TrnklLAVMYk'

# supbabase package stuff
sb = create_client(sb_url, sb_key)

# Function to send data to Supabase
def supa_send(data, table):
    # send the data using supabase package
    insert_data = sb.table(table).insert(data).execute()
    print(insert_data)
    print("Data sent to Supabase.")


