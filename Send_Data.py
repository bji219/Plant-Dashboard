import requests
from supabase_py import create_client # , Client

# Supabase project details
sb_url = 'YOUR-URL-HERE'
sb_key = 'YOUR-KEY-HERE'

# supbabase package stuff
sb = create_client(sb_url, sb_key)

# Function to send data to Supabase
def supa_send(data, table):
    # send the data using supabase package
    insert_data = sb.table(table).insert(data).execute()
    print(insert_data)
    print("Data sent to Supabase.")


